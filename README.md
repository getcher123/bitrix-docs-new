# Документация 1C‑Bitrix (Markdown‑vault)

[![CI](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml/badge.svg)](https://github.com/getcher123/bitrix-docs-new/actions/workflows/ci.yml)

Это офлайн‑хранилище документации 1C‑Bitrix в виде обычных Markdown‑файлов для просмотра в VS Code/Obsidian (без сборщика сайта).

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

Код RAG‑системы находится в `rag/`. Инструкции запуска и конфигурации — в:
- `rag/README.md`
- `docs/RAG/RAG_PLAN.md`

## RAG‑проект: проблема и поведение

**Проблема:** в большом vault Bitrix сложно быстро находить точные ответы, примеры и ссылки на первоисточник.  
**Пользователи:** администраторы и разработчики Bitrix24/1C‑Bitrix.  
**Ограничения:** данные — локальный `docs/` (Markdown‑vault), без внешней индексации.  
**Ожидаемое поведение:** сервис отвечает по источникам, дает ссылки и явно сообщает, когда данных нет.

### User stories (пример)

- Как разработчик, хочу найти пример D7‑класса и получить ссылку на исходную страницу.
- Как разработчик, хочу понять REST‑метод и где он описан.
- Как администратор, хочу найти шаги настройки функциональности (смарт‑процессы/CRM).
- Как пользователь курсов, хочу перейти на нужный урок из ответа.
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

### Demo

- Прод: `https://rag-bitrix-getcher.amvera.io/`
- Smoke: `https://rag-bitrix-getcher.amvera.io/health` (включает `build.git_sha`, если задано)

Как воспроизвести локально:

```bash
make up
make ingest
curl -s http://localhost:8000/health
```

### Локальный запуск (1 команда)

```bash
make up
make ingest
```

## Frontend (bitrix-scribe)

Фронтенд для RAG подключен как git submodule в `frontend/`.  
Сейчас деплой в Amvera настроен **только для backend**; фронтенд будет разворачиваться отдельно.

После клонирования репозитория и при обновлениях:

```bash
git submodule update --init --recursive
```

## API versioning

Версия API фиксируется в `rag/openapi.yaml` (`info.version`) и следует семантическому версионированию:
- `MAJOR` — breaking changes (смена контрактов/ответов)
- `MINOR` — новые эндпоинты/поля
- `PATCH` — исправления без изменения контракта

При изменениях API обновляйте `info.version` и синхронизируйте типы в фронте:

```bash
cd frontend
npm run gen:api
```

## CI/CD (Amvera)

Workflow: `.github/workflows/deploy_amvera.yml`  
Secrets в GitHub:
- `AMVERA_USERNAME`
- `AMVERA_PASSWORD`
- `AMVERA_HEALTH_URL` (опционально, для smoke `/health`)

## Integration tests report

Сгенерировать локальный отчет (CSV/JSON):

```bash
python3 rag/scripts/generate_integration_report.py
```

Файлы отчета:
- `docs/RAG/RAG_INTEGRATION_REPORT.json`
- `docs/RAG/RAG_INTEGRATION_REPORT.csv`

## Источники

- https://dev.1c-bitrix.ru/docs/ (документация, классическое API)
- https://dev.1c-bitrix.ru/api_help/ (классическое API: справочник функций/классов)
- https://dev.1c-bitrix.ru/api_d7/ (D7 API)
- https://dev.1c-bitrix.ru/user_help/ (пользовательская документация)
- https://dev.1c-bitrix.ru/learning/ (учебные курсы)
- https://apidocs.bitrix24.ru/ (Bitrix24 REST API)
- https://github.com/bitrix-tools/b24-rest-docs (upstream-репозиторий Bitrix24 REST, импортирован в `docs/bitrix24_api/b24-rest-docs/`)
