from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv

from bitrix_rag.config import load_config
from bitrix_rag.index.migrate_qdrant import migrate_qdrant_to_pgvector


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    load_dotenv(repo_root / "rag" / ".env")
    cfg = load_config(repo_root)
    result = migrate_qdrant_to_pgvector(repo_root, cfg)
    print(
        "Done. total_points={total_points} inserted={inserted} skipped={skipped} "
        "chunks_loaded={chunks_loaded}".format(**result)
    )


if __name__ == "__main__":
    main()
