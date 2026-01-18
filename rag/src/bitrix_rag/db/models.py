from __future__ import annotations

from datetime import datetime
from typing import Any

from pgvector.sqlalchemy import Vector
from sqlalchemy import DateTime, Float, ForeignKey, Index, Integer, JSON, Text, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class QueryRecord(Base):
    __tablename__ = "queries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query: Mapped[str] = mapped_column(Text, nullable=False)
    sections: Mapped[list[str] | None] = mapped_column(JSON, nullable=True)
    mode: Mapped[str | None] = mapped_column(Text, nullable=True)
    latency_ms: Mapped[float | None] = mapped_column(Float, nullable=True)
    error: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    answers: Mapped[list["AnswerRecord"]] = relationship(
        back_populates="query_record", cascade="all, delete-orphan"
    )
    feedback: Mapped[list["FeedbackRecord"]] = relationship(
        back_populates="query_record", cascade="all, delete-orphan"
    )


class AnswerRecord(Base):
    __tablename__ = "answers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_id: Mapped[int] = mapped_column(
        ForeignKey("queries.id", ondelete="CASCADE"), index=True, nullable=False
    )
    answer_text: Mapped[str] = mapped_column(Text, nullable=False)
    model: Mapped[str | None] = mapped_column(Text, nullable=True)
    tokens: Mapped[int | None] = mapped_column(Integer, nullable=True)
    sources_json: Mapped[Any] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    query_record: Mapped[QueryRecord] = relationship(back_populates="answers")


class FeedbackRecord(Base):
    __tablename__ = "feedback"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    query_id: Mapped[int] = mapped_column(
        ForeignKey("queries.id", ondelete="CASCADE"), index=True, nullable=False
    )
    rating: Mapped[int | None] = mapped_column(Integer, nullable=True)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )

    query_record: Mapped[QueryRecord] = relationship(back_populates="feedback")


class EmbeddingRecord(Base):
    __tablename__ = "embeddings"

    chunk_id: Mapped[str] = mapped_column(Text, primary_key=True)
    content_hash: Mapped[str] = mapped_column(Text, nullable=False)
    path: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    section: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    module: Mapped[str] = mapped_column(Text, nullable=False, index=True)
    title: Mapped[str] = mapped_column(Text, nullable=False)
    heading_path: Mapped[str] = mapped_column(Text, nullable=False)
    text: Mapped[str] = mapped_column(Text, nullable=False)
    embedding: Mapped[list[float]] = mapped_column(
        Vector(1024).with_variant(JSON, "sqlite"), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )


Index("ix_embeddings_section_module", EmbeddingRecord.section, EmbeddingRecord.module)

