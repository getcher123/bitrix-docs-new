from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from ..clients.bge import BgeClient, chunked
from ..ingest.pipeline import ChunkRecord
from .qdrant_store import QdrantStore


@dataclass
class EmbeddingCache:
    values: dict[str, list[float]]

    @classmethod
    def load(cls, path: Path) -> "EmbeddingCache":
        if not path.exists():
            return cls(values={})
        values: dict[str, list[float]] = {}
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            values[row["hash"]] = row["embedding"]
        return cls(values=values)

    def save(self, path: Path) -> None:
        lines = [
            json.dumps({"hash": key, "embedding": value}, ensure_ascii=False)
            for key, value in self.values.items()
        ]
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_vector_index(
    records: list[ChunkRecord],
    store: QdrantStore,
    bge: BgeClient,
    cache_path: Path,
    batch_size: int = 16,
) -> None:
    cache = EmbeddingCache.load(cache_path)
    ids: list[str] = []
    vectors: list[list[float]] = []
    payloads: list[dict] = []

    missing: list[ChunkRecord] = []
    for record in records:
        cached = cache.values.get(record.content_hash)
        if cached is None:
            missing.append(record)
        else:
            ids.append(record.chunk.chunk_id)
            vectors.append(cached)
            payloads.append(_payload(record))

    for batch in chunked(missing, batch_size):
        texts = [item.chunk.text for item in batch]
        embeddings = bge.embed(texts)
        for item, embedding in zip(batch, embeddings):
            cache.values[item.content_hash] = embedding
            ids.append(item.chunk.chunk_id)
            vectors.append(embedding)
            payloads.append(_payload(item))

    if ids:
        store.upsert(ids=ids, vectors=vectors, payloads=payloads)
    cache.save(cache_path)


def _payload(record: ChunkRecord) -> dict:
    payload = {
        "path": record.metadata.path,
        "section": record.metadata.section,
        "module": record.metadata.module,
        "title": record.metadata.title,
        "heading_path": record.metadata.heading_path,
    }
    if record.metadata.course_id:
        payload["course_id"] = record.metadata.course_id
    if record.metadata.lesson_id:
        payload["lesson_id"] = record.metadata.lesson_id
    return payload
