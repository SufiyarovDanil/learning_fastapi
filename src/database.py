import asyncpg
from asyncpg.connection import Connection
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from config import config


async def make_apg_connection() -> Connection:
    return await asyncpg.connect(config.database_uri_asyncpg)


class BaseModel(DeclarativeBase):
    pass


async_engine: AsyncEngine = create_async_engine(
    url=config.database_uri_asyncpg,
    echo=True
)

async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(async_engine)
