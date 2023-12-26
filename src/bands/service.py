from typing import Sequence
from sqlalchemy import select, delete, RowMapping
from sqlalchemy.exc import SQLAlchemyError
from datetime import date
from database import async_session_factory
from .models import BandModel


async def get_all_bands() -> Sequence[RowMapping]:
    async with async_session_factory() as session:
        query = select(BandModel)
        result = await session.execute(query)
    
    return result.mappings().all()


async def get_band_by_id(band_id: int) -> RowMapping | None:
    async with async_session_factory() as session:
        query = select(BandModel).where(BandModel.id == band_id)
        result = await session.execute(query)

    return result.mappings().one_or_none()


async def add_band(name: str, created_at: date = None) -> BandModel | None:
    try:
        async with async_session_factory() as session:
            new_band: BandModel = BandModel(name=name, created_at=created_at)
            session.add(new_band)
            await session.commit()

        return new_band
    except SQLAlchemyError:
        return None


async def update_band(band_id: int, name: str = None, created_at: date = None) -> BandModel | None:
    async with async_session_factory() as session:
        band: BandModel | None = await session.get(BandModel, band_id)

        if band is None:
            return None

        if name is not None:
            band.name = name
        if created_at is not None:
            band.created_at = created_at
        
        await session.commit()

    return band


async def delete_band(band_id: int) -> None:
    async with async_session_factory() as session:
        statement = delete(BandModel).where(BandModel.id == band_id)
        await session.execute(statement)
        await session.commit()


async def is_band_exists(name, created_at: date) -> bool:
    async with async_session_factory() as session:
        query = (
            select(BandModel)
            .where(
                BandModel.name == name
                and BandModel.created_at == created_at
            )
        )

        result = await session.execute(query)
        is_exists: bool = result.one_or_none() is not None

    return is_exists
