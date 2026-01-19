# RAG сервис для Bitrix Markdown‑vault

Этот каталог содержит код RAG‑системы для работы с локальным vault в `../docs/`.

Документация проекта:

- `../docs/RAG/RAG_PLAN.md`
- `../docs/RAG/RAG_PARAMETERS.md`
- `../docs/RAG/RAG_RISKS.md`
- `../docs/RAG/RAG_ACCEPTANCE.md`
- `../docs/RAG/RAG_TEST_SET.md`
- `../docs/RAG/RAG_QUESTIONNAIRE.md`

## Требования

- Python 3.10+
- Docker Desktop (для Qdrant) или локальный Qdrant binary
- Доступ к BGE endpoints (Colab/ngrok)
- OpenAI API key (для генерации ответа; без него будет extractive‑режим)

## Быстрый обзор

- Индексация: `bitrix-rag --env-file .env index`
- Поиск: `bitrix-rag --env-file .env search "запрос"`
- Ответ: `bitrix-rag --env-file .env answer "запрос"`
- API: `uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000`
- Публичный API (ngrok): `./scripts/run_with_ngrok.sh run`

## Проблема и поведение

**Проблема:** в большом Bitrix‑vault сложно быстро находить точные ответы, примеры и ссылки на первоисточник.  
**Пользователи:** администраторы и разработчики Bitrix24/1C‑Bitrix.  
**Ограничения:** данные — локальный `docs/` (Markdown‑vault), без внешней индексации.  
**Ожидаемое поведение:** сервис отвечает по источникам, дает ссылки и явно сообщает, когда данных нет.

### User stories (пример)

- Как разработчик, хочу найти пример D7‑класса и получить ссылку на исходную страницу.
- Как разработчик, хочу понять REST‑метод и где он описан.
- Как администратор, хочу найти шаги настройки функциональности (смарт‑процессы/CRM).
- Как пользователь, хочу перейти на нужный урок из ответа.
- Как пользователь, хочу видеть источники сразу после утверждений.
- Как пользователь, хочу честный ответ “нет данных” и полезную альтернативу.

### Архитектура (high‑level)

```
Frontend (SPA) -> FastAPI /answer
                     |
                     +-> BM25 (rag_data)
                     +-> Vector Search (Postgres+pgvector / Qdrant)
                     +-> Rerank + LLM (OpenAI)
                     +-> Ответ + ссылки
                     +-> История запросов (Postgres/SQLite)
```

## SLA и формат ответа

**Таймауты/SLA (настраиваются через env):**

- `RAG_MAX_LATENCY_S` — общий бюджет ответа (по умолчанию 25s).
- `OPENAI_TIMEOUT_S` — таймаут LLM (по умолчанию 20s).
- `BGE_TIMEOUT_S` — таймаут embed/rerank (по умолчанию 30s).

**Формат ответа API:**

- `answer` — текст ответа без секции `sources:` внутри.
- `sources` — массив путей на источники.
- Если данных нет, ответ **прямо сообщает об этом** и предлагает альтернативы **без ссылок**.

## Frontend

Продовый фронтенд подключен как git submodule в `../frontend/`.

Если после `git clone` папка `frontend/` пустая:

```bash
git submodule update --init --recursive
```

## Единая точка входа

Начинайте с **[docs/MAIN_INDEX.md](docs/MAIN_INDEX.md)** — это единая навигационная страница по ролям и задачам.

## Быстрый старт (2–3 минуты)

### Visual Studio Code (рекомендуется)

1. Откройте папку репозитория в VS Code
2. Откройте `docs/MAIN_INDEX.md`
3. Нажмите `Ctrl+Shift+V` (предпросмотр)
4. `Ctrl+Click` по ссылкам для навигации
5. `Ctrl+Shift+F` для поиска по vault

### Obsidian

1. `Open folder as vault` → выберите папку репозитория (или только `docs/`)
2. Откройте `docs/MAIN_INDEX.md` (или `MAIN_INDEX.md`, если vault = `docs/`)
3. Используйте глобальный поиск и граф ссылок

## Ключевые страницы (без дублирования навигации)

- `docs/MAIN_INDEX.md` — стартовая навигация (единая точка входа)
- `docs/INDEX.md` — индекс разделов (генерируется, пригоден как «карта»)
- `docs/MODULES.md` — список модулей классического API
- `docs/QUICK_REFERENCE.md` — быстрые ответы/сценарии
- `docs/bitrix24_api/index.md` — Bitrix24 REST API (включая импорт `b24-rest-docs`)
- `docs/AGENT.md` — как AI‑агенту искать справку
- `docs/RAG/` — документация по проекту RAG (план, параметры, риски, тесты)
- `docs/ARCHITECTURE.md` — архитектура RAG‑проекта (стек/поток данных)

## Быстрый поиск

```bash
# Поиск по всему хранилищу
rg "CIBlockElement" docs/

# Поиск по заголовкам (класс/метод)
rg "^#\\s+GetList\\b" docs/
```

## RAG‑сервис (опционально)

Код RAG‑системы находится в `rag/`. Полное описание, архитектура, SLA и формат ответов — в:

- `rag/README.md`
- `docs/RAG/RAG_PLAN.md`

## Быстрый запуск (MVP)

1. Поднять Qdrant (если используем):

```bash
docker compose up -d
```

2. Заполнить `.env` по шаблону:

```bash
cp .env.example .env
```

3. Установить зависимости:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

4. Собрать индекс:

```bash
bitrix-rag --env-file .env index
```

5. Запустить API:

```bash
uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000
```

Проверка:

```bash
curl -s http://localhost:8000/health
```

Опционально: запустить API с публичным ngrok‑endpoint:

```bash
chmod +x ./scripts/run_with_ngrok.sh
./scripts/run_with_ngrok.sh run
```

Дальше: индексация и API будут развиваться по плану в `../docs/RAG/RAG_PLAN.md`.

## Dev стенд (Docker + MCP)

Dev‑стенд поднимает API + Postgres + MCP и подхватывает `rag/.env`:

```bash
docker compose -f ../docker-compose.yml -f ../docker-compose.dev.yml up -d db api mcp
```

Проверки:

```bash
curl -s http://localhost:8000/health
python ../mcp/smoke.py
```

Публичный доступ через ngrok (если нужен):

```bash
ngrok http 8000
```

## Конфигурация (.env)

Файл `.env` не коммитится. Основные переменные:

- `VAULT_ROOT=docs` — путь к vault
- `RAG_DATA_DIR=.rag` — локальные артефакты индекса
- `DATABASE_URL=sqlite:///./.rag/app.db` (dev) или `postgresql+psycopg://...` (prod)
- `VECTOR_BACKEND=pgvector` (Postgres+pgvector) или `qdrant` (Qdrant), либо пусто (авто)
- `QDRANT_URL=http://localhost:6333`
- `QDRANT_COLLECTION=bitrix_docs`
- `BGE_PROVIDER=deepinfra` или `colab`
- DeepInfra:
  - `DEEPINFRA_BASE_URL=https://api.deepinfra.com/v1/inference`
  - `DEEPINFRA_EMBED_PATH=/BAAI/bge-m3`
  - `DEEPINFRA_RERANK_PATH=/Qwen/Qwen3-Reranker-0.6B`
  - `DEEPINFRA_KEY=...`
- Colab/ngrok:
- `COLAB_BASE_URL=https://<ngrok>.app`
- `COLAB_EMBED_PATH=/embed`
- `COLAB_RERANK_PATH=/rerank`
- `COLAB_API_KEY=...`
- `OPENAI_API_KEY=...`
- `OPENAI_MODEL=gpt-5.2`
- `OPENAI_BASE_URL=https://api.openai.com/v1`
- `OPENAI_TIMEOUT_S=20`
- `OPENAI_MAX_OUTPUT_TOKENS=800`
- `NGROK_AUTH_TOKEN=...` (для публичного API через ngrok)
- `RAG_EMBED_BATCH=4`
- `RAG_MAX_LATENCY_S=25`
- `RAG_FAST_REST=1` (быстрый режим для REST: без vector/rerank/LLM)

### Пример LLM через DeepInfra (OpenAI‑совместимый API)

```env
OPENAI_BASE_URL=https://api.deepinfra.com/v1/openai
OPENAI_MODEL=Qwen/Qwen3-Next-80B-A3B-Instruct
DEEPINFRA_KEY=...
```

## Миграции (Alembic)

Для PostgreSQL (prod) применить миграции:

```bash
alembic -c alembic.ini upgrade head
```

Для SQLite (dev) таблицы создаются автоматически при старте API.

## История запросов

API сохраняет историю запросов/ответов в БД:

- `queries` — запрос, режим, латентность, ошибки
- `answers` — текст ответа, модель, sources JSON
- `feedback` — оценка/комментарий пользователя (позже подключим UI)

## API endpoints

- `GET /health` — состояние и конфиг
- `POST /search` — топ‑результаты
- `POST /answer` — ответ + источники (`mode`: auto/llm/extractive)
- `GET /history` — последние запросы/ответы
- `GET /openapi.json` — OpenAPI схема

Пример:

```bash
curl -s -X POST http://localhost:8000/answer \
  -H 'Content-Type: application/json' \
  -d '{"query":"Как получить список элементов инфоблока через CIBlockElement::GetList"}'
```

## OpenAPI и debug UI

- Статическая OpenAPI спецификация: `openapi.yaml`
- Фронт‑заглушка для отладки: `debug_frontend/index.html`

Запуск:

1. Запусти API (`uvicorn ...` или `./scripts/run_with_ngrok.sh run`).
2. Открой `http://localhost:8000/debug` (или `${ngrok_url}/debug`).
3. Проверь `POST /answer` или `POST /search`.

## Frontend (отдельно)

В текущем прод‑контейнере Amvera разворачивается **только backend**.  
Frontend планируется деплоить отдельно (Amvera как второй сервис или GitHub Pages).

## Индексация

Индексация создаёт файлы в `.rag/`:

- `chunks.jsonl` — чанки и метаданные
- `bm25.json` — индекс BM25
- `embedding_cache.jsonl` — кеш эмбеддингов
- `index_manifest.json` — mtime/size для инкрементальных обновлений
- `index_version.json` — версия индекса (git commit + timestamp)

Qdrant коллекция: `bitrix_docs`.

Инкрементальная индексация:

```bash
bitrix-rag --env-file .env index --incremental --strategy auto
```

Стратегии: `auto` (git→mtime), `git`, `mtime`.

## Тестирование

Тест‑набор: `../docs/RAG/RAG_TEST_SET.md`  
Отчёт (пример): `../docs/RAG/RAG_TEST_REPORT_FULL.csv`

Оценка recall/MRR:

```bash
python3 scripts/eval_test_set.py --env-file .env --top-k 10 --out ../docs/RAG/RAG_EVAL_REPORT.csv
```

Локальные тесты:

```bash
make test
make test-integration
```

Frontend (unit + e2e):

```bash
cd ../frontend
npm run test
npm run test:e2e
```

## Типичные проблемы

- Qdrant не доступен: проверь `docker compose up -d`, URL и порт `6333`.
- Rerank/Embed дают 4xx/5xx: проверь `BGE_BASE_URL` и ключ.
- LLM ошибки: проверь `OPENAI_MODEL` и `OPENAI_API_KEY`.
- Медленная индексация: уменьшай `RAG_EMBED_BATCH`.
- Логи запросов: `.rag/requests.log` (JSONL, включает timings).

## Остановка

```bash
docker compose down
```

## Источники

- https://dev.1c-bitrix.ru/docs/ (документация, классическое API)
- https://dev.1c-bitrix.ru/api_help/ (классическое API: справочник функций/классов)
- https://dev.1c-bitrix.ru/api_d7/ (D7 API)
- https://dev.1c-bitrix.ru/user_help/ (пользовательская документация)
- https://dev.1c-bitrix.ru/learning/ (учебные курсы)
- https://apidocs.bitrix24.ru/ (Bitrix24 REST API)
- https://github.com/bitrix-tools/b24-rest-docs (upstream-репозиторий Bitrix24 REST, импортирован в `docs/bitrix24_api/b24-rest-docs/`)
