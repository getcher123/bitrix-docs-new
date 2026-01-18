from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import func, select
from sqlalchemy.dialects.postgresql import insert as pg_insert
from sqlalchemy.engine import Engine
from sqlalchemy import text

from ..db.models import EmbeddingRecord


@dataclass(frozen=True)
class PgVectorStore:
    engine: Engine

    def recreate(self) -> None:
        with self.engine.begin() as conn:
            conn.execute(text("TRUNCATE TABLE embeddings"))

    def upsert(
        self,
        ids: list[str],
        vectors: list[list[float]],
        payloads: list[dict],
    ) -> None:
        rows: list[dict] = []
        for chunk_id, vector, payload in zip(ids, vectors, payloads):
            rows.append(
                {
                    "chunk_id": chunk_id,
                    "content_hash": payload.get("content_hash", ""),
                    "path": payload.get("path", ""),
                    "section": payload.get("section", ""),
                    "module": payload.get("module", ""),
                    "title": payload.get("title", ""),
                    "heading_path": payload.get("heading_path", ""),
                    "text": payload.get("text", ""),
                    "embedding": vector,
                }
            )

        if not rows:
            return

        stmt = pg_insert(EmbeddingRecord).values(rows)
        update_cols = {
            "content_hash": stmt.excluded.content_hash,
            "path": stmt.excluded.path,
            "section": stmt.excluded.section,
            "module": stmt.excluded.module,
            "title": stmt.excluded.title,
            "heading_path": stmt.excluded.heading_path,
            "text": stmt.excluded.text,
            "embedding": stmt.excluded.embedding,
            "updated_at": func.now(),
        }
        stmt = stmt.on_conflict_do_update(index_elements=["chunk_id"], set_=update_cols)

        with self.engine.begin() as conn:
            conn.execute(stmt)

    def search(
        self,
        vector: list[float],
        top_k: int,
        sections: list[str] | None = None,
    ) -> list[tuple[str, float]]:
        distance = EmbeddingRecord.embedding.cosine_distance(vector).label("distance")
        stmt = select(EmbeddingRecord.chunk_id, distance)
        if sections:
            stmt = stmt.where(EmbeddingRecord.section.in_(sections))
        stmt = stmt.order_by(distance.asc()).limit(top_k)
        with self.engine.connect() as conn:
            rows = conn.execute(stmt).all()
        return [(row[0], float(row[1])) for row in rows]
