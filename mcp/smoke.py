from __future__ import annotations

import asyncio
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
# Avoid local `mcp/` shadowing the PyPI `mcp` package when run from repo root.
sys.path = [p for p in sys.path if p not in ("", str(REPO_ROOT))]

from mcp import ClientSession, StdioServerParameters, stdio_client  # noqa: E402


def _content_to_text(content: list) -> str:
    parts: list[str] = []
    for item in content:
        if getattr(item, "type", None) == "text":
            parts.append(getattr(item, "text", ""))
    return "\n".join(part for part in parts if part)


async def main() -> None:
    env = os.environ.copy()
    env.setdefault("RAG_ENV_FILE", str(REPO_ROOT / "rag" / ".env"))
    if not Path(env["RAG_ENV_FILE"]).exists():
        env.pop("RAG_ENV_FILE", None)

    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(REPO_ROOT / "mcp" / "server.py")],
        env=env,
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            tool_names = [tool.name for tool in tools.tools]
            print("tools:", tool_names)

            search_result = await session.call_tool(
                "search_docs",
                {"query": "Bitrix VM", "top_k": 3},
            )
            print("search_docs:\n", _content_to_text(search_result.content))

            answer_result = await session.call_tool(
                "answer",
                {"query": "Как получить список элементов инфоблока?", "mode": "extractive"},
            )
            print("answer:\n", _content_to_text(answer_result.content))

            source_result = await session.call_tool(
                "get_source",
                {"path": "docs/MAIN_INDEX.md"},
            )
            print("get_source:\n", _content_to_text(source_result.content)[:400])


if __name__ == "__main__":
    asyncio.run(main())
