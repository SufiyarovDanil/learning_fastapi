import asyncpg
from asyncpg.connection import Connection
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)
from config import (
    DB_NAME,
    DB_HOST,
    DB_PASS,
    DB_PORT,
    DB_USER
)


DATABASE_URI_ASYNCPG: str = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


async def make_apg_connection() -> Connection:
    return await asyncpg.connect(DATABASE_URI_ASYNCPG)


class BaseModel(DeclarativeBase):
    pass


async_engine: AsyncEngine = create_async_engine(
    url=DATABASE_URI_ASYNCPG,
    echo=True
)

async_session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(async_engine)
