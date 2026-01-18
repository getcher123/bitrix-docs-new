.PHONY: up down logs api index index-inc test

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

api:
	PYTHONPATH=rag/src uvicorn bitrix_rag.api.main:app --host 0.0.0.0 --port 8000

index:
	PYTHONPATH=rag/src python3 -m bitrix_rag.cli --env-file rag/.env index

index-inc:
	PYTHONPATH=rag/src python3 -m bitrix_rag.cli --env-file rag/.env index --incremental --strategy auto

test:
	PYTHONPATH=rag/src python3 -m py_compile $(shell find rag/src -type f -name '*.py')
