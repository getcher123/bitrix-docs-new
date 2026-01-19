from __future__ import annotations

import json
from pathlib import Path

from qdrant_client import QdrantClient

from ..config import AppConfig
from ..db import run_migrations
from ..db.engine import create_db_engine
from ..ingest.pipeline import iter_chunks
from .bm25 import Bm25Index
from .pgvector_store import PgVectorStore


def migrate_qdrant_to_pgvector(repo_root: Path, cfg: AppConfig) -> dict[str, int]:
    if not cfg.database.url.startswith("postgres"):
        raise RuntimeError("DATABASE_URL must point to PostgreSQL for pgvector import.")

    run_migrations(repo_root, cfg.database.url)

    chunks_path = cfg.rag_data_dir / "chunks.jsonl"
    if not chunks_path.exists():
        _build_chunks_and_bm25(cfg, chunks_path)

    chunks: dict[str, dict] = {}
    for line in chunks_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        chunk_id = str(row.get("id") or "")
        if chunk_id:
            chunks[chunk_id] = row

    client = QdrantClient(url=cfg.qdrant.url)
    engine = create_db_engine(cfg.database.url)
    store = PgVectorStore(engine)

    total = 0
    inserted = 0
    skipped = 0
    batch_ids: list[str] = []
    batch_vectors: list[list[float]] = []
    batch_payloads: list[dict] = []

    scroll_offset = None
    while True:
        points, scroll_offset = client.scroll(
            collection_name=cfg.qdrant.collection,
            with_payload=True,
            with_vectors=True,
            limit=256,
            offset=scroll_offset,
        )
        if not points:
            break

        for point in points:
            total += 1
            payload = point.payload or {}
            chunk_id = str(payload.get("chunk_id") or point.id)
            chunk_row = chunks.get(chunk_id)
            if not chunk_row:
                skipped += 1
                continue

            vector = point.vector
            if vector is None:
                skipped += 1
                continue

            batch_ids.append(chunk_id)
            batch_vectors.append(vector)
            batch_payloads.append(
                {
                    "content_hash": chunk_row.get("hash", ""),
                    "path": chunk_row.get("path", ""),
                    "section": chunk_row.get("section", ""),
                    "module": chunk_row.get("module", ""),
                    "title": chunk_row.get("title", ""),
                    "heading_path": chunk_row.get("heading_path", ""),
                    "text": chunk_row.get("text", ""),
                }
            )

        if len(batch_ids) >= 512:
            store.upsert(batch_ids, batch_vectors, batch_payloads)
            inserted += len(batch_ids)
            batch_ids.clear()
            batch_vectors.clear()
            batch_payloads.clear()

    if batch_ids:
        store.upsert(batch_ids, batch_vectors, batch_payloads)
        inserted += len(batch_ids)

    return {
        "total_points": total,
        "inserted": inserted,
        "skipped": skipped,
        "chunks_loaded": len(chunks),
    }


def _build_chunks_and_bm25(cfg: AppConfig, chunks_path: Path) -> None:
    records = iter_chunks(
        cfg.vault_root,
        chunk_size=cfg.indexing.chunk_size,
        chunk_overlap=cfg.indexing.chunk_overlap,
        min_chunk=cfg.indexing.min_chunk,
    )
    chunks_path.parent.mkdir(parents=True, exist_ok=True)
    _write_chunks(chunks_path, records)
    bm25 = Bm25Index.build(records)
    bm25.save(cfg.rag_data_dir / "bm25.json")


def _write_chunks(path: Path, records: list) -> None:
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
