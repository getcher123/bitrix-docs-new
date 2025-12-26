# Структура проекта RAG (предлагаемая)

Цель — отделить:
- **vault‑контент** (в `docs/`, `images/`) от
- **кода RAG** (в `rag/`) и
- **runtime‑артефактов** (индексы/кеши в `.rag/` или `rag_data/`, не коммитятся).

## Где что лежит

- Документация по проекту RAG:
  - `docs/RAG_PLAN.md` — план и чекбоксы прогресса
  - `docs/RAG_PARAMETERS.md` — параметры и стек (в т.ч. Colab endpoints)
  - `docs/RAG_RISKS.md` — риски и минимизация
  - `docs/RAG_ACCEPTANCE.md` — критерии тестирования/приемки
  - `docs/RAG_TEST_SET.md` — контрольные вопросы с эталонными ссылками
  - `docs/RAG_QUESTIONNAIRE.md` — ответы на вводные вопросы (настроечный “источник правды”)

- Код и инфраструктура RAG: `rag/`

## Дерево `rag/`

```
rag/
  README.md                 # как запустить/обновить (MVP)
  pyproject.toml            # зависимости и tooling
  .env.example              # шаблон переменных окружения
  docker-compose.yml        # локальная Qdrant (опционально)
  src/bitrix_rag/
    config.py               # конфигурация из env (BGE/OpenAI/Qdrant)
    ingest/                 # загрузка/очистка/чанкинг Markdown
    clients/                # клиенты к внешним сервисам (BGE endpoints, OpenAI)
    index/                  # построение/обновление индексов (vector + bm25)
    retrieval/              # роутинг, гибридный retrieval, rerank
    api/                    # FastAPI (/health, /search, /answer)
    cli.py                  # CLI для индексации и запросов (MVP)
```

## Runtime‑данные (не коммитятся)

- `.rag/` или `rag_data/` — кеш эмбеддингов, промежуточные jsonl, артефакты индексации.

Исключения уже добавлены в `.gitignore`.
