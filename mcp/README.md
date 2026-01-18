# MCP server for Bitrix docs

This MCP server exposes Bitrix Markdown‑vault tools for search/answer/source lookup.

## Requirements

- Python 3.10+
- Vault indexed in `.rag/` (`make ingest` from repo root)
- Dependencies installed: `pip install -e rag`

The server reads `.env` from `rag/.env` by default. You can override with:

```bash
export RAG_ENV_FILE=/path/to/.env
```

## Run

```bash
python mcp/server.py
```

Note: run the script directly (not `python -m mcp.server`) to avoid module name
collisions with the PyPI `mcp` package.

## Tools

- `search_docs(query, top_k=10, filters={section,module,path_prefix})`
- `answer(query, mode=auto|llm|extractive)`
- `get_source(path)` (path relative to `docs/`)

## Smoke test

```bash
python mcp/smoke.py
```

## Client config examples

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "bitrix-docs": {
      "command": "python",
      "args": ["mcp/server.py"],
      "env": {
        "RAG_ENV_FILE": "rag/.env"
      }
    }
  }
}
```

### VS Code / Cursor (MCP config)

```json
{
  "mcpServers": {
    "bitrix-docs": {
      "command": "python",
      "args": ["mcp/server.py"],
      "env": {
        "RAG_ENV_FILE": "rag/.env"
      }
    }
  }
}
```
