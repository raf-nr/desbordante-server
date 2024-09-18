from typing import Generator

from sqlalchemy import create_engine, NullPool
from sqlalchemy.orm import sessionmaker, Session

from internal.infrastructure.data_storage import settings

DataStorageContext = Session

default_engine = create_engine(url=settings.postgres_dsn.unicode_string())
engine_without_pool = create_engine(
    url=settings.postgres_dsn.unicode_string(),
    poolclass=NullPool,
)

ContextLocal = sessionmaker(bind=default_engine)
ContextLocalWithoutPool = sessionmaker(bind=engine_without_pool)


def get_context() -> Generator[DataStorageContext, None, None]:
    """
    Returns a generator that yields a context(session) object for database operations.
    """
    with ContextLocal() as context:
        yield context

def get_context_without_pool() -> Generator[DataStorageContext, None, None]:
    """
    Returns a generator that yields a context(session) object without pool for database operations.
    """
    with ContextLocalWithoutPool() as context:
        yield context
