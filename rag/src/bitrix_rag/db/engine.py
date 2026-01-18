from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


@dataclass(frozen=True)
class Database:
    engine: Engine
    Session: sessionmaker


def create_db_engine(database_url: str, *, echo: bool = False) -> Engine:
    connect_args: dict = {}
    if database_url.startswith("sqlite:"):
        connect_args["check_same_thread"] = False
    return create_engine(
        database_url,
        echo=echo,
        future=True,
        pool_pre_ping=True,
        connect_args=connect_args,
    )


def create_session_factory(engine: Engine) -> sessionmaker:
    return sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)

