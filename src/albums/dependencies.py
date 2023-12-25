from sqlalchemy import RowMapping
from .schemas import AlbumCreate, AlbumUpdate
from . import service
from . import exceptions as exc


async def valid_album_id(album_id: int) -> RowMapping:
    album: RowMapping | None = await service.get_album_by_id(album_id)

    if album is None:
        raise exc.AlbumNotFound()

    return album


async def valid_creating_album(album: AlbumCreate) -> None:
    exists: bool = await service.is_album_exists(album.name, album.band_id, album.published_at)

    if exists:
        raise exc.AlbumAlreadyExists()


async def valid_updating_album(album: AlbumUpdate) -> None:
    await valid_album_id(album.id)
