# TODO по критериям проекта (DataTalksClub AI Dev Tools Zoomcamp)

Цель: закрыть **все 12 критериев** (максимальные баллы), с учетом принятых решений:

- Репозиторий публичный, включает полный `docs/` (личный проект). (Q1 обновлено)
- Деплой: **Amvera Cloud** (Dockerfile + `amvera.yml` + managed services; `docker compose` — локально/CI). (Q2=A)
- Аудитория: **смешанная** (админы + разработчики). (Q3=C)
- Публичный доступ **без авторизации** (но с тех. защитами). (Q4=C)
- DB: **Postgres (prod) + SQLite (dev/test)**; вектора в Postgres через **pgvector** (Qdrant опционально). (Q5=A)
- Frontend: **React+Vite SPA** + тесты. (Q6=A)
- OpenAPI: `openapi.yaml` — **контракт**, из него генерируем клиент/типы. (Q7=A)
- CI/CD: тесты + деплой на Amvera. (Q8=A)
- MCP: **свой MCP server** в репо. (Q9=A)
- Индексация: **incremental + full rebuild по команде**. (Q10=A)
- Политика “нет источников”: **явно говорить и давать альтернативы без ссылок**. (Q11=A)
- Нагрузка: **A** (демо/малый прод). (Q12=A)

Ссылки на существующую документацию:
- План RAG: `docs/RAG/RAG_PLAN.md`
- Параметры: `docs/RAG/RAG_PARAMETERS.md`
- Критерии приемки: `docs/RAG/RAG_ACCEPTANCE.md`
- Риски: `docs/RAG/RAG_RISKS.md`
- Тест‑набор: `docs/RAG/RAG_TEST_SET.md`
- Структура проекта: `docs/RAG/RAG_PROJECT_STRUCTURE.md`

---

## Текущее состояние инфраструктуры (зафиксировано)

**Amvera (проект `rag-bitrix`)**
- ID: `119309`
- Status: `RUN_FAILED` (последняя ошибка: `FileNotFoundError: /app/.rag/requests.log`)
- Instances: `requires=1`, `current=0`
- Tariff (текущий): `BEGINNER_PLUS` (0.5 CPU / 1 GB RAM / 7 GB SSD)
- Domain (internal): `amvera-getcher-run-rag-bitrix`
- Git clone/remote:
  - `git clone https://git.amvera.ru/getcher/rag-bitrix`
  - `git remote add amvera https://git.amvera.ru/getcher/rag-bitrix`
- Build log (последняя ошибка):
  - `lstat /workspace/frontend/package.json: no such file or directory`

**Amvera Postgres (managed, pgvector)**
- Текущая БД: `ps-db2` (`PS-DB2`, `RUNNING`)
- Предыдущая БД: `ps-db` (`PS-DB`, `STOPPED`)
- DB name: `PS-DB`
- Owner: `USER-DB`
- Superuser access: включен
- Расширение `vector` (pgvector): включено (подтверждено пользователем)
- INTERNAL домены: `amvera-getcher-cnpg-ps-db2-rw` (rw), `amvera-getcher-cnpg-ps-db2-ro` (ro)
- Лимиты (tariff): 0.5 CPU / 1 GB RAM / 25 GB SSD (`amvera tariff --slug ps-db2`)

**Frontend**
- Подключен как submodule: `frontend/`
- Репозиторий: `https://github.com/getcher123/bitrix-scribe.git` (branch `main`)
- Деплой через **GitHub Pages** (отдельно от backend).
- Требует доработки под критерии (SPA + тесты + единый API‑клиент + экраны Ask/History/Eval).

---

## Этап 0 — “Гигиена репозитория” (обязательное до публичного релиза)

- [x] Убедиться, что секреты не закоммичены: `rag/.env`, токены ngrok, ключи OpenAI/DeepInfra.
- [x] Добавить/проверить `.gitignore` для: `.env`, `.rag/`, `rag_data/`, `__pycache__/`, `.venv/`, `node_modules/`, `dist/`.
- [ ] Ротация скомпрометированных ключей (если когда-либо попадали в git/логи/чат).
- [ ] Описать политику данных: что хранится, где, как удалить (GDPR‑подобный минимум).

---

## 1) Problem description (README) — 2/2

- [x] В корневом `README.md` описать: проблему, пользователей (админ+dev), ограничения (vault не публичный), expected behavior.
- [x] Добавить “User stories” (5–8 штук): поиск по D7, по REST, по курсам, “нет данных в базе”, “с источниками/без”.
- [x] Добавить схему high-level (1 картинка или ASCII): Frontend → API → Retrieval → (Postgres+pgvector/DB/LLM).
- [ ] (ожидает пользователя) Раздел “Demo”: ссылка на прод‑URL (Amvera) + как воспроизвести локально.
  - URL: `https://rag-bitrix-getcher.amvera.io/` (получен от пользователя, добавить в README)

**Критерий готовности**
- README объясняет “что это” за 1 минуту чтения + есть ссылка на рабочий демо‑URL.

---

## 2) AI system development (tools, workflow, MCP) — 2/2

- [x] В `AGENT.md` (и/или `docs/`) описать workflow разработки (инструменты, промпты, правила, как обновлять план).
- [x] Добавить “How we used AI tools”: какие задачи, какие правила, какие ограничения.
- [x] Реализовать **MCP server** в репо: `mcp/` (или `rag/mcp/`) с инструментами:
  - [x] `search_docs(query, top_k, filters)`
  - [x] `answer(query, mode?)`
  - [x] `get_source(path)` (для выдачи конкретного чанка/страницы)
- [x] Документация подключения MCP (VS Code / Claude Desktop / Codex): где конфиг, как запускать.
- [x] Добавить минимальные тесты MCP (smoke): запуск, вызов 2–3 инструментов.

**Критерий готовности**
- В репо есть реальный MCP server + инструкции + демонстрация использования.

---

## 3) Technologies & architecture — 2/2

- [x] В `README.md` или `docs/ARCHITECTURE.md` описать стек:
  - Frontend: React+Vite
  - Backend: FastAPI
  - Vector DB: Postgres + pgvector (prod), Qdrant (опционально)
  - DB: Postgres/SQLite (SQLAlchemy)
  - LLM: OpenAI (Responses API для `gpt-5.*`)
  - Embeddings/Rerank: выбранный провайдер (DeepInfra/Colab) и ограничения
  - Infra: docker compose + Amvera + CI/CD
- [x] Описать поток данных: ingestion → chunking → embed → upsert → retrieval → rerank → prompt → answer.
- [x] Описать observability: логи, метрики латентности, трассировка шагов.

---

## 4) Front-end — 3/3

- [x] Создать `frontend/` (React+Vite) с единой точкой общения с API (client module):
  - [x] Экран “Ask”: вопрос → ответ + источники (только после утверждений).
  - [x] Экран “History”: последние запросы/ответы (из DB).
  - [x] Экран “Eval/Smoke”: прогон тест‑набора + таблица результатов.
- [x] Добавить настройки в UI: base URL (локально/прод), таймаут, режим (llm/extractive/auto).
- [x] Добавить unit‑тесты фронта (Vitest): клиент API, парсинг sources, отображение ошибок.
- [x] Добавить e2e (Playwright): “задал вопрос → получил ответ → вижу источники”.

---

## 5) API contract (OpenAPI) — 2/2

- [x] Привести `rag/openapi.yaml` к фактическому API (или наоборот — привести API к контракту).
- [x] Генерация клиента для фронта из OpenAPI (например, `openapi-typescript` + fetch wrapper).
- [x] Добавить CI-проверку: OpenAPI не “сломали” (lint/validate).
- [ ] Документировать версии API (semver/changes).

---

## 6) Back-end — 3/3

- [x] Привести структуру `rag/src/bitrix_rag` к чистым слоям: `api/`, `retrieval/`, `clients/`, `db/`, `ingest/`, `eval/`.
- [x] Добавить тесты backend:
  - [x] unit: роутер/фильтры/форматирование sources/citations
  - [x] unit: OpenAI client (mock)
  - [x] unit: embed/rerank clients (mock)
  - [x] integration: FastAPI endpoint `/answer` (TestClient) + sqlite/postgres
- [ ] Гарантировать SLA по таймаутам: `RAG_MAX_LATENCY_S`, `OPENAI_TIMEOUT_S`, per-step timeouts.
- [ ] Единый формат ответа: `answer` без “sources:” текста внутри; источники — в `sources` (и/или отдельный `citations` массив).

---

## 7) Database integration — 2/2

- [x] Добавить слой DB (SQLAlchemy):
  - [x] таблица `queries` (query, mode, latency_ms, error, created_at)
  - [x] таблица `answers` (answer_text, model, tokens, sources_json)
  - [x] таблица `feedback` (rating, comment)
- [x] Добавить векторное хранилище в Postgres (pgvector):
  - [x] `CREATE EXTENSION IF NOT EXISTS vector;`
  - [x] таблица `embeddings` (`chunk_id`, `path`, `section`, `embedding vector(1024)`, ...)
  - [x] индекс по вектору (HNSW/IVFFLAT) + стратегия обновления
- [x] Проверка в `/health`: DB доступна, `pgvector` включен.
- [x] Конфиг окружений:
  - [x] `DATABASE_URL=sqlite:///...` для dev/test
  - [x] `DATABASE_URL=postgresql+psycopg://...` для prod
- [x] Миграции (Alembic) + команда “init/upgrade”.
- [x] Документация: где посмотреть историю, как чистить.

---

## 8) Containerization — 2/2

- [x] `docker-compose.yml` для локального полного стека: `api`, `postgres(+pgvector)`, `frontend` (nginx).
- [x] `amvera.yml` для деплоя в Amvera (Dockerfile + managed services).
- [ ] (ожидает пользователя) `Dockerfile` (prod) — сборка backend + сборка/встраивание frontend (или отдельный контейнер, если Amvera это поддерживает). Сейчас деплой backend‑only.
- [x] `make up/down/logs/test` (или `justfile`) для удобства.
- [x] Локальный запуск “одной командой” согласно README.

---

## 9) Integration testing — 2/2

- [x] Отдельный набор integration tests (pytest marker `integration`):
  - [x] использует FastAPI TestClient + sqlite (без docker)
  - [x] выполняет ключевые сценарии: answer, search, history
- [ ] Отчет по прогону (CSV/JSON) с latency и flags (answer_has_sources, exact/whitelist).
- [x] Документация: как запускать локально и в CI.

---

## 10) Deployment — 2/2

- [ ] Описать “как деплоим на Amvera” (infra-as-doc):
  - [ ] переменные окружения
  - [ ] managed Postgres (pgvector): подключение rw/ro + `DATABASE_URL`
  - [ ] healthchecks
  - [ ] внешний домен/публичный URL (для demo/peer-review)
- [ ] (опционально) Поднять Qdrant как отдельный проект/сервис в Amvera и подключить по внутренней сети (в `QDRANT_URL`) если pgvector не устроит.
- [ ] Дать рабочий прод‑URL (в README) + доказательство (скрин/лог deploy).
- [ ] Smoke endpoint: `/health` + версия сборки (git sha).

---

## 11) CI/CD — 2/2

- [x] GitHub Actions CI:
  - [x] lint (python + frontend)
  - [x] unit tests (backend+frontend)
  - [x] integration tests (docker compose)
  - [x] OpenAPI validation
- [ ] (ожидает пользователя) CD:
  - [ ] deploy job на Amvera: `amvera rebuild` через GitHub Actions (нужны `AMVERA_USERNAME`/`AMVERA_PASSWORD` secrets)
  - [ ] после деплоя — smoke check `/health` (нужен `AMVERA_HEALTH_URL` secret)
- [x] Badge в README (CI status).

---

## 12) Reproducibility — 2/2

- [x] “One-command” локальный старт: `make up` или `docker compose up -d`.
- [x] “One-command” тесты: `make test` (unit) и `make test-integration`.
- [x] “One-command” ingestion: `make ingest` (по `docs/`).
- [ ] Опционально для ускорения CI: `demo_vault/` (20–50 файлов) + `make ingest-demo`.

---

## Рекомендуемый минимальный тариф (из предложенных)

Для выбранной архитектуры (API + Postgres(pgvector) + frontend; embeddings/rerank внешние) и нагрузки A:

- [ ] (ожидает пользователя) Решение по тарифу: **не повышаем** (остаёмся на `BEGINNER_PLUS`).

---

## Порядок выполнения (предлагаемый)

1) Этап 0 (секреты/чистота) → 2) Docker-compose full stack → 3) DB слой + миграции → 4) Frontend SPA + OpenAPI client → 5) CI (unit) → 6) Integration tests → 7) CD deploy Amvera → 8) MCP server + docs → 9) Финальная полировка README/Architecture.

---

## Результаты опроса (Amvera/Deploy)

- Формат деплоя (Amvera): один проект (Dockerfile) = **backend**; frontend — **GitHub Pages**.
- Submodule фронта: `bitrix-scribe` делаем публичным и используем HTTPS URL для `frontend/` в `.gitmodules`.
- Демо/peer-review: внешний URL `https://rag-bitrix-getcher.amvera.io/`.
- Данные: публикуем полный `docs/` (без отдельного demo dataset).
- Embeddings/rerank (prod): облачный провайдер (DeepInfra) + ключи в env Amvera.
- CD: GitHub Actions пушит в Amvera git remote и запускает сборку/деплой.
