from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy import RowMapping
from . import service
from .dependencies import valid_band_id, valid_updating_band, valid_creating_band
from .schemas import BandCreate, BandUpdate


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Band']
)


@router.get('/band/')
async def get_all_bands() -> JSONResponse:
    band_list = await service.get_all_bands()
    
    return JSONResponse(content=jsonable_encoder(band_list), status_code=200)


@router.get('/band/{id}')
async def get_band_by_id(band: RowMapping = Depends(valid_band_id)) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(band), status_code=200)


@router.post('/band', dependencies=[Depends(valid_creating_band)])
async def add_band(band: BandCreate) -> Response:
    await service.add_band(band.name, band.created_at)

    return Response(status_code=200)


@router.put('/band', dependencies=[Depends(valid_updating_band)])
async def update_band(band: BandUpdate) -> Response:
    await service.update_band(band.id, band.name, band.created_at)

    return Response(status_code=200)


@router.delete('/band', dependencies=[Depends(valid_band_id)])
async def delete_band(band_id: int) -> Response:
    await service.delete_band(band_id)

    return Response(status_code=200)
