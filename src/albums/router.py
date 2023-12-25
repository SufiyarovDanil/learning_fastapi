from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy import RowMapping
from . import service
from .dependencies import valid_album_id, valid_creating_album, valid_updating_album
from .schemas import AlbumCreate, AlbumUpdate


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Album']
)


@router.get('/album/')
async def get_all_albums() -> JSONResponse:
    album_list = await service.get_all_albums()
    
    return JSONResponse(content=jsonable_encoder(album_list), status_code=200)


@router.get('album/{id}')
async def get_album_by_id(album: RowMapping = Depends(valid_album_id)) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(album), status_code=200)


@router.post('/album', dependencies=[Depends(valid_creating_album)])
async def add_album(album: AlbumCreate) -> Response:
    await service.add_album(album.name, album.band_id, album.published_at)

    return Response(status_code=200)


@router.put('/album', dependencies=[Depends(valid_updating_album)])
async def update_album(album: AlbumUpdate) -> Response:
    await service.update_album(
        album.id,
        album.name,
        album.band_id,
        album.published_at
    )

    return Response(status_code=200)


@router.delete('/album', dependencies=[Depends(valid_album_id)])
async def delete_album(album_id: int) -> Response:
    await service.delete_album(album_id)

    return Response(status_code=200)
