from __future__ import annotations

import json
from pathlib import Path

from dotenv import load_dotenv
from qdrant_client import QdrantClient

from bitrix_rag.config import load_config
from bitrix_rag.db import run_migrations
from bitrix_rag.index.pgvector_store import PgVectorStore
from bitrix_rag.db.engine import create_db_engine


def _load_chunks(chunks_path: Path) -> dict[str, dict]:
    if not chunks_path.exists():
        raise FileNotFoundError(f"Chunks file not found: {chunks_path}")
    items: dict[str, dict] = {}
    for line in chunks_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        chunk_id = str(row.get("id") or "")
        if not chunk_id:
            continue
        items[chunk_id] = row
    return items


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    load_dotenv(repo_root / "rag" / ".env")
    cfg = load_config(repo_root)

    if not cfg.database.url.startswith("postgres"):
        raise RuntimeError("DATABASE_URL must point to PostgreSQL for pgvector import.")

    run_migrations(repo_root, cfg.database.url)

    chunks_path = cfg.rag_data_dir / "chunks.jsonl"
    chunks = _load_chunks(chunks_path)

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

    print(
        f"Done. total_points={total} inserted={inserted} skipped={skipped} "
        f"chunks_loaded={len(chunks)}"
    )


if __name__ == "__main__":
    main()
