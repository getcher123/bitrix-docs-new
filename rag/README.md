# RAG сервис для Bitrix Markdown‑vault

Этот каталог содержит код RAG‑системы для работы с локальным vault в `../docs/`.

Документация проекта:
- `../docs/RAG/RAG_PLAN.md`
- `../docs/RAG/RAG_PARAMETERS.md`
- `../docs/RAG/RAG_RISKS.md`
- `../docs/RAG/RAG_ACCEPTANCE.md`
- `../docs/RAG/RAG_TEST_SET.md`
- `../docs/RAG/RAG_QUESTIONNAIRE.md`

## Быстрый запуск (MVP)

1) Поднять Qdrant (если используем):

```bash
docker compose up -d
```

2) Заполнить `.env` по шаблону:

```bash
cp .env.example .env
```

3) Установить зависимости:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e .
```

4) Собрать индекс:

```bash
bitrix-rag --env-file .env index
```

5) Запустить API:

```bash
uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000
```

Проверка:

```bash
curl -s http://localhost:8000/health
```

Дальше: индексация и API будут развиваться по плану в `../docs/RAG/RAG_PLAN.md`.
