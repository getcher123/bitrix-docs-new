"""init db tables

Revision ID: 0001_init_db
Revises:
Create Date: 2026-01-18

"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa


revision = "0001_init_db"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "queries",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("query", sa.Text(), nullable=False),
        sa.Column("sections", sa.JSON(), nullable=True),
        sa.Column("mode", sa.Text(), nullable=True),
        sa.Column("latency_ms", sa.Float(), nullable=True),
        sa.Column("error", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    op.create_table(
        "answers",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("query_id", sa.Integer(), sa.ForeignKey("queries.id", ondelete="CASCADE"), nullable=False),
        sa.Column("answer_text", sa.Text(), nullable=False),
        sa.Column("model", sa.Text(), nullable=True),
        sa.Column("tokens", sa.Integer(), nullable=True),
        sa.Column("sources_json", sa.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_answers_query_id", "answers", ["query_id"])

    op.create_table(
        "feedback",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("query_id", sa.Integer(), sa.ForeignKey("queries.id", ondelete="CASCADE"), nullable=False),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column("comment", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )
    op.create_index("ix_feedback_query_id", "feedback", ["query_id"])

    bind = op.get_bind()
    dialect = bind.dialect.name

    if dialect == "postgresql":
        op.execute("CREATE EXTENSION IF NOT EXISTS vector")

        try:
            from pgvector.sqlalchemy import Vector

            embedding_type = Vector(1024)
        except Exception:
            embedding_type = sa.JSON()

        op.create_table(
            "embeddings",
            sa.Column("chunk_id", sa.Text(), primary_key=True),
            sa.Column("content_hash", sa.Text(), nullable=False),
            sa.Column("path", sa.Text(), nullable=False),
            sa.Column("section", sa.Text(), nullable=False),
            sa.Column("module", sa.Text(), nullable=False),
            sa.Column("title", sa.Text(), nullable=False),
            sa.Column("heading_path", sa.Text(), nullable=False),
            sa.Column("text", sa.Text(), nullable=False),
            sa.Column("embedding", embedding_type, nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        )
        op.create_index("ix_embeddings_path", "embeddings", ["path"])
        op.create_index("ix_embeddings_section", "embeddings", ["section"])
        op.create_index("ix_embeddings_module", "embeddings", ["module"])
        op.create_index("ix_embeddings_section_module", "embeddings", ["section", "module"])

        op.execute(
            "CREATE INDEX IF NOT EXISTS ix_embeddings_embedding_hnsw "
            "ON embeddings USING hnsw (embedding vector_cosine_ops)"
        )
    else:
        op.create_table(
            "embeddings",
            sa.Column("chunk_id", sa.Text(), primary_key=True),
            sa.Column("content_hash", sa.Text(), nullable=False),
            sa.Column("path", sa.Text(), nullable=False),
            sa.Column("section", sa.Text(), nullable=False),
            sa.Column("module", sa.Text(), nullable=False),
            sa.Column("title", sa.Text(), nullable=False),
            sa.Column("heading_path", sa.Text(), nullable=False),
            sa.Column("text", sa.Text(), nullable=False),
            sa.Column("embedding", sa.JSON(), nullable=False),
            sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        )
        op.create_index("ix_embeddings_path", "embeddings", ["path"])
        op.create_index("ix_embeddings_section", "embeddings", ["section"])
        op.create_index("ix_embeddings_module", "embeddings", ["module"])
        op.create_index("ix_embeddings_section_module", "embeddings", ["section", "module"])


def downgrade() -> None:
    op.drop_index("ix_embeddings_section_module", table_name="embeddings")
    op.drop_index("ix_embeddings_module", table_name="embeddings")
    op.drop_index("ix_embeddings_section", table_name="embeddings")
    op.drop_index("ix_embeddings_path", table_name="embeddings")
    op.drop_table("embeddings")

    op.drop_index("ix_feedback_query_id", table_name="feedback")
    op.drop_table("feedback")

    op.drop_index("ix_answers_query_id", table_name="answers")
    op.drop_table("answers")

    op.drop_table("queries")

