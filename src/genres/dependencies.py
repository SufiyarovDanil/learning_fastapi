from sqlalchemy import RowMapping
from .schemas import GenreCreate, GenreUpdate
from . import service
from . import exceptions as exc


async def valid_genre_id(genre_id: int) -> RowMapping:
    genre: RowMapping | None = await service.get_genre_by_id(genre_id)

    if genre is None:
        raise exc.GenreNotFound()

    return genre


async def valid_creating_genre(genre: GenreCreate) -> None:
    exists: bool = await service.is_genre_exists(genre.name)

    if exists:
        raise exc.GenreAlreadyExists()


async def valid_updating_genre(genre: GenreUpdate) -> None:
    await valid_genre_id(genre.id)
