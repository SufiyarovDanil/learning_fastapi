from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from . import service
from .schemas import Band as BandSchema


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Band']
)


@router.get('/band/')
async def get_all_bands() -> JSONResponse:
    band_list = await service.get_all_bands()

    if len(band_list) == 0:
        return JSONResponse(content=None, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(band_list), status_code=200)


@router.get('band/{id}')
async def get_band_by_id(id: int) -> JSONResponse:
    band = await service.get_band_by_id(id)

    if band is None:
        return JSONResponse(content=None, status_code=400)

    return JSONResponse(content=jsonable_encoder(band), status_code=200)


@router.post('/band')
async def add_band(band: BandSchema) -> Response:
    await service.add_band(band.name, band.created_at)

    return Response(status_code=200)


@router.put('/band')
async def update_band(band: BandSchema) -> Response:
    await service.update_band(band.id, band.name, band.created_at)

    return Response(status_code=200)


@router.delete('/band')
async def delete_band(id: int) -> Response:
    await service.delete_band(id)

    return Response(status_code=200)
