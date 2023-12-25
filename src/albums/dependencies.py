from sqlalchemy import RowMapping
from . import service
from . import exceptions as exc


async def valid_album_id(album_id: int) -> RowMapping:
    album: RowMapping | None = await service.get_album_by_id(album_id)

    if album is None:
        raise exc.AlbumNotFound()

    return album
