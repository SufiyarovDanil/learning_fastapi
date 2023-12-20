from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from . import service
from schemas import Album as AlbumSchema


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Album']
)


@router.get('/album/')
async def get_all_albums() -> JSONResponse:
    album_list = await service.get_all_albums()

    if len(album_list) == 0:
        return JSONResponse(content=None, status_code=400)
    
    return JSONResponse(content=jsonable_encoder(album_list), status_code=200)


@router.get('album/{id}')
async def get_album_by_id(id: int) -> JSONResponse:
    band = await service.get_album_by_id(id)

    if band is None:
        return JSONResponse(content=None, status_code=400)

    return JSONResponse(content=jsonable_encoder(band), status_code=200)


@router.post('/album')
async def add_band(album: AlbumSchema) -> Response:
    await service.add_album(album.name, album.band_id, album.published_at)

    return Response(status_code=200)


@router.put('/album')
async def update_album(album: AlbumSchema) -> Response:
    await service.update_album(
        album.id,
        album.name,
        album.band_id,
        album.published_at
    )

    return Response(status_code=200)


@router.delete('/album')
async def delete_album(id: int) -> Response:
    await service.delete_album(id)

    return Response(status_code=200)
