from sqlalchemy import select, delete
from datetime import date
from database import async_session_factory
from .models import AlbumModel


async def get_all_albums() -> list[AlbumModel]:
    async with async_session_factory() as session:
        query = select(AlbumModel)
        result = await session.execute(query)
    
    return result.mappings().all()


async def get_album_by_id(id: int) -> AlbumModel | None:
    async with async_session_factory() as session:
        query = select(AlbumModel).where(AlbumModel.id == id)
        result = await session.execute(query)

    return result.mappings().one_or_none()


async def add_album(name: str, band_id: int, published_at: date = None) -> None:
    async with async_session_factory() as session:
        new_album: AlbumModel = AlbumModel(name=name, published_at=published_at, band_id=band_id)
        session.add(new_album)
        await session.commit()


async def update_album(id: int, name: str = None, band_id: int = None, published_at: date = None) -> None:
    async with async_session_factory() as session:
        album: AlbumModel = session.get(AlbumModel, id)

        if album is None:
           return # TODO create exception for this

        if name is not None:
            album.name = name
        if band_id is not None:
            album.band_id = band_id
        if published_at is not None:
            album.published_at = published_at
        
        await session.commit()


async def delete_album(id: int) -> None:
    async with async_session_factory() as session:
        statement = delete(AlbumModel).where(AlbumModel.id == id)
        await session.execute(statement)
        await session.commit()
