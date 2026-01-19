from __future__ import annotations

from pathlib import Path

from alembic import command
from alembic.config import Config


def run_migrations(repo_root: Path, database_url: str) -> None:
    config_path = repo_root / "rag" / "alembic.ini"
    alembic_dir = repo_root / "rag" / "alembic"
    config = Config(str(config_path))
    config.set_main_option("script_location", str(alembic_dir))
    config.set_main_option("sqlalchemy.url", database_url)
    command.upgrade(config, "head")
