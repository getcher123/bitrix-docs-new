from __future__ import annotations

import argparse
from pathlib import Path

from dotenv import load_dotenv

from .config import load_config


def main() -> None:
    parser = argparse.ArgumentParser(prog="bitrix-rag")
    parser.add_argument("--env-file", default=".env", help="Path to .env (default: .env)")
    args = parser.parse_args()

    env_path = Path(args.env_file)
    if env_path.exists():
        load_dotenv(env_path)

    repo_root = Path(__file__).resolve().parents[3]
    cfg = load_config(repo_root)

    print("bitrix-rag config:")
    print(f"- vault_root: {cfg.vault_root}")
    print(f"- qdrant: {cfg.qdrant.url} (collection={cfg.qdrant.collection})")
    print(f"- bge_base_url: {cfg.bge.base_url or '[not set]'}")
    print(f"- openai_model: {cfg.openai.model}")

