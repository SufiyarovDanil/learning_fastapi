from fastapi import APIRouter
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from . import service
from .exceptions import AlbumNotFound
from .schemas import AlbumCreate, AlbumUpdate


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Album']
)


@router.get('/album/')
async def get_all_albums() -> JSONResponse:
    album_list = await service.get_all_albums()

    if len(album_list) == 0:
        raise AlbumNotFound()
    
    return JSONResponse(content=jsonable_encoder(album_list), status_code=200)


@router.get('album/{id}')
async def get_album_by_id(album_id: int) -> JSONResponse:
    band = await service.get_album_by_id(album_id)

    if band is None:
        raise AlbumNotFound()

    return JSONResponse(content=jsonable_encoder(band), status_code=200)


@router.post('/album')
async def add_band(album: AlbumCreate) -> Response:
    await service.add_album(album.name, album.band_id, album.published_at)

    return Response(status_code=200)


@router.put('/album')
async def update_album(album: AlbumUpdate) -> Response:
    await service.update_album(
        album.id,
        album.name,
        album.band_id,
        album.published_at
    )

    return Response(status_code=200)


@router.delete('/album')
async def delete_album(album_id: int) -> Response:
    await service.delete_album(album_id)

    return Response(status_code=200)
