from __future__ import annotations

import csv
import json
import os
import time
from pathlib import Path
from tempfile import TemporaryDirectory

from fastapi.testclient import TestClient

from bitrix_rag.api.main import create_app
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


def _timed_request(client: TestClient, method: str, path: str, json_body: dict | None = None) -> dict:
    start = time.perf_counter()
    response = client.request(method, path, json=json_body)
    latency_ms = (time.perf_counter() - start) * 1000
    return {
        "method": method,
        "path": path,
        "status_code": response.status_code,
        "latency_ms": round(latency_ms, 2),
        "ok": response.status_code == 200,
        "response_body": response.json() if response.headers.get("content-type", "").startswith("application/json") else None,
    }


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    report_dir = repo_root / "docs" / "RAG"
    report_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        rag_dir = tmp_path / ".rag"
        _write_test_indexes(rag_dir)

        os.environ["RAG_DATA_DIR"] = str(rag_dir)
        os.environ["VAULT_ROOT"] = str(tmp_path / "docs")
        os.environ["DATABASE_URL"] = f"sqlite:///{tmp_path / 'app.db'}"
        os.environ["VECTOR_BACKEND"] = "none"
        os.environ["BGE_BASE_URL"] = "http://localhost:9999"
        os.environ["OPENAI_API_KEY"] = ""
        os.environ["RAG_FAST_REST"] = "1"

        app = create_app()
        client = TestClient(app)

        results = [
            _timed_request(client, "GET", "/health"),
            _timed_request(client, "POST", "/search", {"query": "REST api"}),
            _timed_request(client, "POST", "/answer", {"query": "REST api"}),
            _timed_request(client, "GET", "/history?limit=20"),
        ]

    json_path = report_dir / "RAG_INTEGRATION_REPORT.json"
    csv_path = report_dir / "RAG_INTEGRATION_REPORT.csv"

    json_path.write_text(json.dumps({"results": results}, ensure_ascii=False, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["method", "path", "status_code", "latency_ms", "ok"])
        writer.writeheader()
        for row in results:
            writer.writerow({k: row[k] for k in writer.fieldnames})

    print(f"Saved report: {json_path}")
    print(f"Saved report: {csv_path}")


if __name__ == "__main__":
    main()
