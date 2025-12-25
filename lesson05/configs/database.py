from fastapi import Request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from configs.env import settings_config

settings = settings_config()


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.database_url,
    echo=True,
    pool_pre_ping=True,
    pool_size=settings.pool_size,
    max_overflow=settings.max_overflow,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


