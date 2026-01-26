# Bitrix Docs Vault + RAG (Zoomcamp Project)

[![CI](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml/badge.svg)](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml)

Этот README раскрывает проект **по критериям** из Zoomcamp (DataTalksClub AI Dev Tools) и ведет к подробной документации.

---

## 1) Problem description

**Проблема:** в большом Bitrix‑vault сложно быстро находить точные ответы, примеры и ссылки на первоисточник.  
**Пользователи:** администраторы и разработчики Bitrix24/1C‑Bitrix.  
**Ограничения:** данные — локальный `docs/` (Markdown‑vault), без внешней индексации.

User stories (кратко):
- Найти пример D7‑класса и получить ссылку на исходную страницу.
- Найти REST‑метод и его документацию.
- Найти шаги настройки функциональности (смарт‑процессы/CRM).
- Видеть источники сразу после утверждений.
- Получать честный ответ “данных нет” + альтернативы без ссылок.

---

## 2) Data & policy

**Храним:** `docs/`, индексы (`.rag/`, `.rag_demo/`), историю запросов/ответов в БД.  
**Не храним:** пароли/ключи в репозитории; секреты только в env.  
**Удаление:** удалить `.rag/`/`.rag_demo/`; очистить таблицы `queries`, `answers`, `feedback`, `embeddings`.

---

## 3) Architecture & tech stack

Стек:
- Frontend: React + Vite (SPA)
- Backend: FastAPI
- Vector: Postgres + pgvector (prod), Qdrant (опционально)
- DB: Postgres (prod) / SQLite (dev)
- LLM: OpenAI (Responses API)
- Embeddings/Rerank: DeepInfra/Colab
- Infra: Docker, Amvera, GitHub Actions

High‑level поток:
```
Frontend -> FastAPI /answer
   -> BM25 + Vector Search (pgvector/Qdrant)
   -> Rerank + LLM
   -> Answer + sources + History
```

---

## 4) AI tools / MCP

В репозитории есть MCP‑server с инструментами:
- `search_docs(query, top_k, filters)`
- `answer(query, mode?)`
- `get_source(path)`

Документация: `docs/AGENT.md` и `mcp/`.

---

## 5) API contract (OpenAPI)

Контракт: `rag/openapi.yaml`  
Генерация типов фронта:
```bash
cd frontend
npm run gen:api
```

Версионирование API — semver в `info.version` (OpenAPI).

---

## 6) Backend

Код: `rag/src/bitrix_rag/`  
Слои: `api/`, `retrieval/`, `clients/`, `db/`, `ingest/`, `eval/`.

SLA/таймауты настраиваются через env:
`RAG_MAX_LATENCY_S`, `OPENAI_TIMEOUT_S`, `BGE_TIMEOUT_S`.

Формат ответа:
- `answer` без текста `sources:` внутри
- `sources` отдельным массивом
- если данных нет — честный ответ + альтернативы без ссылок

---

## 7) Frontend

Submodule: `frontend/` → `https://github.com/getcher123/bitrix-scribe`  
Экраны: Ask / History / Eval.  
Тесты: unit (Vitest) + e2e (Playwright).

---

## 8) Database & Vector store

Postgres + pgvector:
- таблицы `queries`, `answers`, `feedback`, `embeddings`
- миграции Alembic
- `/health` показывает статус DB и pgvector

---

## 9) Evaluation & tests

Unit + integration tests, CI‑отчет:
- `docs/RAG/RAG_INTEGRATION_REPORT.json`
- `docs/RAG/RAG_INTEGRATION_REPORT.csv`

Сгенерировать локально:
```bash
python3 rag/scripts/generate_integration_report.py
```

---

## 10) Deployment (Amvera)

Прод: `https://rag-bitrix-getcher.amvera.io/`  
Smoke: `https://rag-bitrix-getcher.amvera.io/health`

Документация деплоя: `docs/RAG/AMVERA_DEPLOY.md`

---

## 11) CI/CD

CI workflow: `.github/workflows/ci.yml`  
CD workflow: `.github/workflows/cd.yml`  
Secrets:
- `AMVERA_USERNAME`
- `AMVERA_PASSWORD`
- `AMVERA_HEALTH_URL`

---

## 12) Reproducibility

Локальный запуск:
```bash
make up
make ingest
```

Demo‑ingest для CI:
```bash
make ingest-demo
```

---

## Дополнительно

Полная документация RAG:
- `rag/README.md`
- `docs/RAG/` (план, параметры, тесты, риски)

Единая точка входа по документации Bitrix:
- `docs/MAIN_INDEX.md`

---
