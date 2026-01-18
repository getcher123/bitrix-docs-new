from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]
# Avoid local `mcp/` shadowing the PyPI `mcp` package when run from repo root.
sys.path = [p for p in sys.path if p not in ("", str(REPO_ROOT))]

from mcp.server.fastmcp import FastMCP  # noqa: E402

RAG_SRC = REPO_ROOT / "rag" / "src"
sys.path.insert(0, str(RAG_SRC))

from bitrix_rag.config import load_config  # noqa: E402
from bitrix_rag.retrieval.rag import RagService, _extractive_answer  # noqa: E402


def _load_env() -> None:
    env_path = os.environ.get("RAG_ENV_FILE")
    if env_path:
        load_dotenv(env_path)
        return
    default_env = REPO_ROOT / "rag" / ".env"
    if default_env.exists():
        load_dotenv(default_env)


_load_env()
CFG = load_config(REPO_ROOT)
SERVICE = RagService(CFG)

mcp = FastMCP("bitrix-docs-mcp")


@mcp.tool()
def search_docs(
    query: str,
    top_k: int = 10,
    filters: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Search documents in the vault. Filters: section, module, path_prefix."""
    results = SERVICE.search(query)
    if filters:
        section = filters.get("section")
        module = filters.get("module")
        path_prefix = filters.get("path_prefix")
        if section:
            results = [doc for doc in results if doc.section == section]
        if module:
            results = [doc for doc in results if doc.module == module]
        if path_prefix:
            results = [doc for doc in results if doc.path.startswith(path_prefix)]
    items = results[: max(1, int(top_k))]
    return {
        "query": query,
        "results": [
            {
                "path": doc.path,
                "title": doc.title,
                "heading_path": doc.heading_path,
                "section": doc.section,
                "module": doc.module,
            }
            for doc in items
        ],
    }


@mcp.tool()
def answer(query: str, mode: str = "auto") -> dict[str, Any]:
    """Answer a question. mode: auto | llm | extractive."""
    mode = (mode or "auto").lower()
    if mode not in {"auto", "llm", "extractive"}:
        return {"error": f"Unsupported mode: {mode}"}

    if mode == "extractive":
        candidates = SERVICE.search(query)
        if not candidates:
            return {
                "answer": "Не найдено в локальном индексе. Попробуйте уточнить запрос.",
                "sources": [],
                "mode": "fallback",
                "timings_ms": {},
            }
        sources = [f"docs/{doc.path}" for doc in candidates[:4]]
        return {
            "answer": _extractive_answer(query, candidates),
            "sources": sources,
            "mode": "extractive",
            "timings_ms": {},
        }

    result = SERVICE.answer(query)
    if mode == "llm" and result.get("mode") != "llm":
        result["warning"] = "LLM was requested but fallback mode was used."
    return result


@mcp.tool()
def get_source(path: str) -> dict[str, Any]:
    """Return markdown content by path (relative to docs/)."""
    if not path:
        return {"error": "Empty path"}
    rel = path.replace("\\", "/")
    if rel.startswith("docs/"):
        rel = rel[5:]
    safe_path = (CFG.vault_root / rel).resolve()
    if CFG.vault_root not in safe_path.parents or not safe_path.exists():
        return {"error": f"Not found: {path}"}
    content = safe_path.read_text(encoding="utf-8", errors="ignore")
    return {"path": f"docs/{rel}", "content": content}


if __name__ == "__main__":
    mcp.run()
