from typing import Sequence
from sqlalchemy import select, delete, RowMapping
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from database import async_session_factory
from .models import AlbumModel


async def get_all_albums(with_tracks: bool = False) -> Sequence[RowMapping]:
    async with async_session_factory() as session:
        query = select(AlbumModel)

        if with_tracks:
            query = query.options(joinedload(AlbumModel.tracks))

        result = await session.execute(query)

    return result.unique().mappings().all() if with_tracks else result.mappings().all()


async def get_album_by_id(album_id: int, with_tracks: bool = False) -> RowMapping | None:
    async with async_session_factory() as session:
        query = select(AlbumModel).where(AlbumModel.id == album_id)

        if with_tracks:
            query = query.options(joinedload(AlbumModel.tracks))

        result = await session.execute(query)

    return result.unique().mappings().one_or_none() if with_tracks else result.mappings().one_or_none()


async def add_album(name: str, band_id: int, published_at: date = None) -> AlbumModel | None:
    try:
        async with async_session_factory() as session:
            new_album: AlbumModel = AlbumModel(name=name, published_at=published_at, band_id=band_id)
            session.add(new_album)
            await session.commit()

        return new_album
    except SQLAlchemyError:
        return None


async def update_album(
        album_id: int,
        name: str = None,
        band_id: int = None,
        published_at: date = None
) -> AlbumModel | None:
    async with async_session_factory() as session:
        album: AlbumModel | None = await session.get(AlbumModel, album_id)

        if album is None:
            return None

        if name is not None:
            album.name = name
        if band_id is not None:
            album.band_id = band_id
        if published_at is not None:
            album.published_at = published_at

        await session.commit()

        return album


async def delete_album(album_id: int) -> None:
    async with async_session_factory() as session:
        statement = delete(AlbumModel).where(AlbumModel.id == album_id)
        await session.execute(statement)
        await session.commit()


async def is_album_exists(name: str, band_id: int, published_at: date) -> bool:
    async with async_session_factory() as session:
        query = (
            select(AlbumModel)
            .where(
                AlbumModel.name == name
                and AlbumModel.band_id == band_id
                and AlbumModel.published_at == published_at
            )
        )

        result = await session.execute(query)
        is_exists: bool = result.one_or_none() is not None

    return is_exists
