from __future__ import annotations

import json
from pathlib import Path

from ..clients.bge import BgeClient
from ..config import AppConfig
from ..ingest.pipeline import ChunkRecord, iter_chunks
from .bm25 import Bm25Index
from .qdrant_store import QdrantStore
from .vector_index import build_vector_index


CHUNKS_FILE = "chunks.jsonl"
BM25_FILE = "bm25.json"
EMBED_CACHE_FILE = "embedding_cache.jsonl"


def build_indexes(cfg: AppConfig) -> None:
    cfg.rag_data_dir.mkdir(parents=True, exist_ok=True)
    records = iter_chunks(
        cfg.vault_root,
        chunk_size=cfg.indexing.chunk_size,
        chunk_overlap=cfg.indexing.chunk_overlap,
        min_chunk=cfg.indexing.min_chunk,
    )

    _write_chunks(cfg.rag_data_dir / CHUNKS_FILE, records)

    bm25 = Bm25Index.build(records)
    bm25.save(cfg.rag_data_dir / BM25_FILE)

    try:
        store = QdrantStore.connect(
            url=cfg.qdrant.url,
            collection=cfg.qdrant.collection,
            vector_size=1024,
        )
        bge = BgeClient(cfg.bge)
        build_vector_index(
            records,
            store=store,
            bge=bge,
            cache_path=cfg.rag_data_dir / EMBED_CACHE_FILE,
            batch_size=cfg.indexing.embed_batch_size,
            max_text_chars=cfg.indexing.max_rerank_chars,
        )
    except Exception as exc:
        print(f"Vector index skipped (qdrant unavailable): {exc}")


def _write_chunks(path: Path, records: list[ChunkRecord]) -> None:
    lines = []
    for record in records:
        lines.append(
            json.dumps(
                {
                    "id": record.chunk.chunk_id,
                    "text": record.chunk.text,
                    "path": record.metadata.path,
                    "section": record.metadata.section,
                    "module": record.metadata.module,
                    "title": record.metadata.title,
                    "heading_path": record.metadata.heading_path,
                    "course_id": record.metadata.course_id,
                    "lesson_id": record.metadata.lesson_id,
                    "hash": record.content_hash,
                },
                ensure_ascii=False,
            )
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
