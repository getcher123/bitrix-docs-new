# Архитектура проекта (RAG для Bitrix)

Этот документ описывает текущий стек, поток данных и наблюдаемость.

## Стек

- Frontend: React + Vite (отдельный деплой)
- Backend: FastAPI
- Vector DB: Postgres + pgvector (prod), Qdrant (опционально)
- DB: Postgres/SQLite (SQLAlchemy + Alembic)
- LLM: OpenAI (Responses API для `gpt-5.*`)
- Embeddings/Rerank: DeepInfra или Colab (выбор через `.env`)
- Infra: Docker Compose (локально), Amvera (prod)

## Поток данных

```
docs/ (Markdown) -> ingest -> chunking -> embed -> upsert
                                         |
query -> router -> BM25 + vector -> rerank -> prompt -> answer + sources
                                            |
                                            +-> history (DB)
```

## Наблюдаемость

- Логи запросов: `.rag/requests.log` (JSONL, timings)
- Метрики латентности: `timings_ms` в ответах `/answer`
- Health‑check: `/health` (доступность DB, pgvector, индексы)

## Ограничения и допущения

- Источник знаний — локальный vault `docs/`.
- Ответы строятся только на доступных источниках; если нет — сервис сообщает об этом.
- Frontend и backend деплоятся отдельно.
