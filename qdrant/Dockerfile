FROM qdrant/qdrant:latest

# Ensure snapshots are stored on the persistent mount (see qdrant/amvera.yaml).
ENV QDRANT__STORAGE__SNAPSHOTS_PATH=/qdrant/storage/snapshots

COPY qdrant/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 6333

ENTRYPOINT ["/entrypoint.sh"]
