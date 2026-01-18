from __future__ import annotations

from pathlib import Path
import json
import logging
import time
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from ..config import load_config
from ..retrieval.rag import RagService
from ..retrieval.router import route_sections


class SearchRequest(BaseModel):
    query: str


class AnswerRequest(BaseModel):
    query: str


def create_app() -> FastAPI:
    repo_root = Path(__file__).resolve().parents[4]
    load_dotenv(repo_root / "rag" / ".env")
    cfg = load_config(repo_root)

    app = FastAPI(title="bitrix-rag")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*", "ngrok-skip-browser-warning"],
    )
    service = RagService(cfg)
    log_path = cfg.rag_data_dir / "requests.log"
    logger = _setup_request_logger(log_path)
    debug_dir = repo_root / "rag" / "debug_frontend"
    if debug_dir.exists():
        app.mount("/debug", StaticFiles(directory=str(debug_dir), html=True), name="debug")

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
        request_id = uuid.uuid4().hex[:8]
        started = time.time()
        result = service.answer(req.query)
        latency_ms = (time.time() - started) * 1000
        _log_request(
            logger,
            request_id=request_id,
            query=req.query,
            sections=route_sections(req.query),
            result=result,
            latency_ms=latency_ms,
        )
        return result

    return app


def _setup_request_logger(log_path: Path) -> logging.Logger:
    logger = logging.getLogger("bitrix_rag.requests")
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    return logger


def _log_request(
    logger: logging.Logger,
    request_id: str,
    query: str,
    sections: list[str],
    result: dict,
    latency_ms: float,
) -> None:
    payload = {
        "request_id": request_id,
        "query": query,
        "sections": sections,
        "mode": result.get("mode"),
        "sources_count": len(result.get("sources") or []),
        "timings_ms": result.get("timings_ms") or {},
        "latency_ms": round(latency_ms, 2),
    }
    logger.info(json.dumps(payload, ensure_ascii=False))


app = create_app()
