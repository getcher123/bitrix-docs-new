from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import text
from sqlalchemy.engine import Engine


@dataclass(frozen=True)
class DatabaseHealth:
    ok: bool
    dialect: str
    pgvector: bool | None
    error: str | None


def check_database_health(engine: Engine) -> DatabaseHealth:
    dialect = engine.dialect.name
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
            pgvector: bool | None = None
            if dialect == "postgresql":
                row = conn.execute(
                    text("SELECT 1 FROM pg_extension WHERE extname = 'vector' LIMIT 1")
                ).fetchone()
                pgvector = bool(row)
        return DatabaseHealth(ok=True, dialect=dialect, pgvector=pgvector, error=None)
    except Exception as exc:
        return DatabaseHealth(
            ok=False,
            dialect=dialect,
            pgvector=None,
            error=str(exc)[:500],
        )

