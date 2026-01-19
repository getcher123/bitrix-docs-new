import json
import os
from pathlib import Path

from fastapi.testclient import TestClient

from bitrix_rag.index.bm25 import tokenize


def _write_test_indexes(rag_dir: Path) -> None:
    rag_dir.mkdir(parents=True, exist_ok=True)
    chunk_id = "doc-1"
    text = "REST API usage guide"
    chunk = {
        "id": chunk_id,
        "text": text,
        "path": "rest/example.md",
        "title": "REST Example",
        "heading_path": "Intro",
        "section": "REST",
        "module": "rest",
    }
    (rag_dir / "chunks.jsonl").write_text(json.dumps(chunk, ensure_ascii=False) + "\n", encoding="utf-8")
    bm25_payload = {"doc_ids": [chunk_id], "tokens": [tokenize(text)]}
    (rag_dir / "bm25.json").write_text(json.dumps(bm25_payload, ensure_ascii=False), encoding="utf-8")


def test_api_search_answer_history(tmp_path, monkeypatch):
    rag_dir = tmp_path / ".rag"
    _write_test_indexes(rag_dir)

    monkeypatch.setenv("RAG_DATA_DIR", str(rag_dir))
    monkeypatch.setenv("VAULT_ROOT", str(tmp_path / "docs"))
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{tmp_path / 'app.db'}")
    monkeypatch.setenv("VECTOR_BACKEND", "none")
    monkeypatch.setenv("BGE_BASE_URL", "http://localhost:9999")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    monkeypatch.setenv("RAG_FAST_REST", "1")
    monkeypatch.setenv("SKIP_APP_INIT", "1")

    from bitrix_rag.api.main import create_app

    app = create_app()
    client = TestClient(app)

    health = client.get("/health")
    assert health.status_code == 200

    search = client.post("/search", json={"query": "REST api"})
    assert search.status_code == 200
    search_data = search.json()
    assert search_data["results"][0]["path"] == "rest/example.md"

    answer = client.post("/answer", json={"query": "REST api"})
    assert answer.status_code == 200
    answer_data = answer.json()
    assert answer_data["mode"] in {"extractive", "fallback", "llm"}
    assert "docs/rest/example.md" in answer_data.get("sources", [])

    history = client.get("/history")
    assert history.status_code == 200
    history_data = history.json()
    assert history_data["items"]
    assert history_data["items"][0]["query"] == "REST api"
