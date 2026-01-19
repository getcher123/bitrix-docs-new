from __future__ import annotations

import json
from pathlib import Path

from qdrant_client import QdrantClient

from ..config import AppConfig
from ..db import run_migrations
from ..db.engine import create_db_engine
from .pgvector_store import PgVectorStore


def migrate_qdrant_to_pgvector(repo_root: Path, cfg: AppConfig) -> dict[str, int]:
    if not cfg.database.url.startswith("postgres"):
        raise RuntimeError("DATABASE_URL must point to PostgreSQL for pgvector import.")

    run_migrations(repo_root, cfg.database.url)

    chunks_path = cfg.rag_data_dir / "chunks.jsonl"
    if not chunks_path.exists():
        raise FileNotFoundError(f"Chunks file not found: {chunks_path}")

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
