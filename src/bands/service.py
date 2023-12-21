from sqlalchemy import select, delete
from datetime import date
from database import async_session_factory
from .models import BandModel


async def get_all_bands() -> list[BandModel]:
    async with async_session_factory() as session:
        query = select(BandModel)
        result = await session.execute(query)
    
    return result.mappings().all()


async def get_band_by_id(id: int) -> BandModel | None:
    async with async_session_factory() as session:
        query = select(BandModel).where(BandModel.id == id)
        result = await session.execute(query)

    return result.mappings().one_or_none()


async def add_band(name: str, created_at: date = None) -> None:
    async with async_session_factory() as session:
        new_band: BandModel = BandModel(name=name, created_at=created_at)
        session.add(new_band)
        await session.commit()


async def update_band(id: int, name: str = None, created_at: date = None) -> None:
    async with async_session_factory() as session:
        band: BandModel = await session.get(BandModel, id)

        if band is None:
            return # TODO create exception for this

        if name is not None:
            band.name = name
        if created_at is not None:
            band.created_at = created_at
        
        await session.commit()


async def delete_band(id: int) -> None:
    async with async_session_factory() as session:
        statement = delete(BandModel).where(BandModel.id == id)
        session.execute(statement)
        await session.commit()
