from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path

from ..clients.bge import BgeClient, chunked
import uuid
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
    max_text_chars: int = 2000,
) -> None:
    cache = EmbeddingCache.load(cache_path)
    missing: list[ChunkRecord] = []
    for record in records:
        cached = cache.values.get(record.content_hash)
        if cached is None:
            missing.append(record)
        else:
            store.upsert(
                ids=[_point_id(record.chunk.chunk_id)],
                vectors=[cached],
                payloads=[_payload(record)],
            )

    total_batches = max(1, (len(missing) + batch_size - 1) // batch_size)
    batch_idx = 0
    for batch in chunked(missing, batch_size):
        batch_idx += 1
        if batch_idx == 1 or batch_idx % 25 == 0 or batch_idx == total_batches:
            print(f"Embedding batch {batch_idx}/{total_batches} (batch_size={batch_size})")
        texts = [item.chunk.text[:max_text_chars] for item in batch]
        batch_ids: list[str] = []
        batch_vectors: list[list[float]] = []
        batch_payloads: list[dict] = []
        try:
            embeddings = bge.embed(texts)
            for item, embedding in zip(batch, embeddings):
                cache.values[item.content_hash] = embedding
                batch_ids.append(_point_id(item.chunk.chunk_id))
                batch_vectors.append(embedding)
                batch_payloads.append(_payload(item))
        except Exception as exc:
            if len(batch) == 1:
                print(f"Embed failed for {batch[0].chunk.chunk_id}: {exc}")
                continue
            print(f"Embed batch failed, retrying single items: {exc}")
            for item in batch:
                try:
                    embedding = bge.embed([item.chunk.text[:max_text_chars]])[0]
                except Exception as item_exc:
                    print(f"Embed failed for {item.chunk.chunk_id}: {item_exc}")
                    continue
                cache.values[item.content_hash] = embedding
                batch_ids.append(_point_id(item.chunk.chunk_id))
                batch_vectors.append(embedding)
                batch_payloads.append(_payload(item))

        if batch_ids:
            store.upsert(ids=batch_ids, vectors=batch_vectors, payloads=batch_payloads)
    cache.save(cache_path)


def _payload(record: ChunkRecord) -> dict:
    payload = {
        "chunk_id": record.chunk.chunk_id,
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


def _point_id(chunk_id: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, chunk_id))
