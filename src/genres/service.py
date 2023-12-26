from typing import Sequence
from sqlalchemy import select, delete, RowMapping
from sqlalchemy.exc import SQLAlchemyError
from database import async_session_factory
from .models import GenreModel


async def get_all_genres() -> Sequence[RowMapping]:
    async with async_session_factory() as session:
        query = select(GenreModel)
        result = await session.execute(query)

    return result.mappings().all()


async def get_genre_by_id(genre_id: int) -> RowMapping | None:
    async with async_session_factory() as session:
        query = select(GenreModel).where(GenreModel.id == genre_id)
        result = await session.execute(query)

    return result.mappings().one_or_none()


async def add_genre(name: str) -> GenreModel | None:
    try:
        async with async_session_factory() as session:
            new_genre: GenreModel = GenreModel(name=name)
            session.add(new_genre)
            await session.commit()

        return new_genre
    except SQLAlchemyError:
        return None


async def update_genre(genre_id: int, name: str = None) -> GenreModel | None:
    async with async_session_factory() as session:
        genre: GenreModel | None = await session.get(GenreModel, genre_id)

        if genre is None:
            return None

        if name is not None:
            genre.name = name

        await session.commit()

    return genre


async def delete_genre(genre_id: int) -> None:
    async with async_session_factory() as session:
        statement = delete(GenreModel).where(GenreModel.id == genre_id)
        await session.execute(statement)
        await session.commit()


async def is_genre_exists(name: str) -> bool:
    async with async_session_factory() as session:
        query = select(GenreModel).where(GenreModel.id == genre_id and GenreModel.name == name)
        result = await session.execute(query)
        is_exists: bool = result.one_or_none() is not None

    return is_exists
