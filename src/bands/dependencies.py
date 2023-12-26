from sqlalchemy import RowMapping
from .schemas import BandCreate, BandUpdate
from . import service
from . import exceptions as exc


async def valid_band_id(band_id: int) -> RowMapping:
    band: RowMapping | None = await service.get_band_by_id(band_id)

    if band is None:
        raise exc.BandNotFound()

    return band


async def valid_creating_band(band: BandCreate) -> None:
    exists: bool = await service.is_band_exists(band.name, band.created_at)

    if exists:
        raise exc.BandAlreadyExists()


async def valid_updating_band(band: BandUpdate) -> None:
    await valid_band_id(band.id)
