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

Публичный URL (будет активирован после успешной сборки в Amvera):  
`https://rag-bitrix-getcher.amvera.io`

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

## Источники

- https://dev.1c-bitrix.ru/docs/ (документация, классическое API)
- https://dev.1c-bitrix.ru/api_help/ (классическое API: справочник функций/классов)
- https://dev.1c-bitrix.ru/api_d7/ (D7 API)
- https://dev.1c-bitrix.ru/user_help/ (пользовательская документация)
- https://dev.1c-bitrix.ru/learning/ (учебные курсы)
- https://apidocs.bitrix24.ru/ (Bitrix24 REST API)
- https://github.com/bitrix-tools/b24-rest-docs (upstream-репозиторий Bitrix24 REST, импортирован в `docs/bitrix24_api/b24-rest-docs/`)
