FROM qdrant/qdrant:latest

# Ensure storage and snapshots are stored on the persistent mount (see qdrant/amvera.yaml).
ENV QDRANT__STORAGE__PATH=/qdrant/storage
ENV QDRANT__STORAGE__SNAPSHOTS_PATH=/qdrant/storage/snapshots

USER root
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates tar \
  && rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 6333

ENTRYPOINT ["/entrypoint.sh"]
