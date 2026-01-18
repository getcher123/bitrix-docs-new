FROM python:3.10-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/rag/src

RUN pip install --no-cache-dir -U pip

# Install backend deps (editable) while keeping source tree for correct repo_root resolution.
COPY rag/pyproject.toml /app/rag/pyproject.toml
COPY rag/src /app/rag/src
RUN pip install --no-cache-dir -e /app/rag

# Runtime files
COPY rag/openapi.yaml /app/rag/openapi.yaml
COPY rag/debug_frontend /app/rag/debug_frontend
COPY docs /app/docs
COPY metadata.json /app/metadata.json
COPY url_mapping.json /app/url_mapping.json

EXPOSE 8000

CMD ["uvicorn", "bitrix_rag.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

