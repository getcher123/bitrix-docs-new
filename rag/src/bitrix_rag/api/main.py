from __future__ import annotations

from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ..config import load_config
from ..retrieval.rag import RagService


def create_app() -> FastAPI:
    repo_root = Path(__file__).resolve().parents[4]
    load_dotenv(repo_root / "rag" / ".env")
    cfg = load_config(repo_root)

    app = FastAPI(title="bitrix-rag")
    service = RagService(cfg)

    class SearchRequest(BaseModel):
        query: str

    class AnswerRequest(BaseModel):
        query: str

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

    @app.post("/search")
    def search(req: SearchRequest):
        if not req.query.strip():
            raise HTTPException(status_code=400, detail="Empty query")
        results = service.search(req.query)
        return {
            "query": req.query,
            "results": [
                {
                    "path": doc.path,
                    "title": doc.title,
                    "heading_path": doc.heading_path,
                    "section": doc.section,
                    "module": doc.module,
                }
                for doc in results
            ],
        }

    @app.post("/answer")
    def answer(req: AnswerRequest):
        if not req.query.strip():
            raise HTTPException(status_code=400, detail="Empty query")
        return service.answer(req.query)

    return app


app = create_app()
