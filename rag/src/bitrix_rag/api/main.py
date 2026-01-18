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
from sqlalchemy.orm import sessionmaker

from ..config import load_config
from ..db import AnswerRecord, Base, QueryRecord, check_database_health, create_db_engine, create_session_factory
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

    db_engine = create_db_engine(cfg.database.url)
    db_session_factory: sessionmaker = create_session_factory(db_engine)
    if cfg.database.url.startswith("sqlite:"):
        Base.metadata.create_all(db_engine)

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
        db_health = check_database_health(db_engine)
        return {
            "status": "ok",
            "vault_root": str(cfg.vault_root),
            "rag_data_dir": str(cfg.rag_data_dir),
            "indexes_present": {
                "chunks": (cfg.rag_data_dir / "chunks.jsonl").exists(),
                "bm25": (cfg.rag_data_dir / "bm25.json").exists(),
            },
            "database": {
                "ok": db_health.ok,
                "dialect": db_health.dialect,
                "pgvector": db_health.pgvector,
                "error": db_health.error,
            },
            "vector_backend": cfg.vector_store.backend,
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
        sections = route_sections(req.query)
        started = time.time()
        result = service.answer(req.query)
        latency_ms = (time.time() - started) * 1000
        _log_request(
            logger,
            request_id=request_id,
            query=req.query,
            sections=sections,
            result=result,
            latency_ms=latency_ms,
        )
        _persist_request(
            db_session_factory,
            query=req.query,
            sections=sections,
            result=result,
            latency_ms=latency_ms,
            model=cfg.openai.model,
        )
        return result

    frontend_dir = repo_root / "frontend_dist"
    if frontend_dir.exists():
        # Mount after API routes to keep /health, /search, /answer working.
        app.mount("/", StaticFiles(directory=str(frontend_dir), html=True), name="frontend")

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


def _persist_request(
    session_factory: sessionmaker,
    query: str,
    sections: list[str],
    result: dict,
    latency_ms: float,
    model: str,
) -> None:
    try:
        with session_factory() as session:
            query_record = QueryRecord(
                query=query,
                sections=sections,
                mode=result.get("mode"),
                latency_ms=round(float(latency_ms), 2),
                error=result.get("error"),
            )
            session.add(query_record)
            session.flush()
            session.add(
                AnswerRecord(
                    query_id=query_record.id,
                    answer_text=str(result.get("answer") or ""),
                    model=model,
                    tokens=None,
                    sources_json=result.get("sources") or [],
                )
            )
            session.commit()
    except Exception:
        # Never fail the API request because DB logging failed.
        return


app = create_app()
