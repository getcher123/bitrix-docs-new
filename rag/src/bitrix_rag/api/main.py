from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI

from ..config import load_config


def create_app() -> FastAPI:
    repo_root = Path(__file__).resolve().parents[4]
    load_dotenv(repo_root / "rag" / ".env")
    cfg = load_config(repo_root)

    app = FastAPI(title="bitrix-rag")

    @app.get("/health")
    def health():
        return {
            "status": "ok",
            "vault_root": str(cfg.vault_root),
            "qdrant_url": cfg.qdrant.url,
            "qdrant_collection": cfg.qdrant.collection,
            "bge_base_url_set": bool(cfg.bge.base_url),
            "openai_model": cfg.openai.model,
        }

    return app


app = create_app()

