from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder
from sqlalchemy import RowMapping
from . import service
from .dependencies import valid_genre_id, valid_updating_genre, valid_creating_genre
from .schemas import GenreCreate, GenreUpdate


router: APIRouter = APIRouter(
    prefix='/music',
    tags=['Genre']
)


@router.get('/genre/')
async def get_all_genres() -> JSONResponse:
    genre_list = await service.get_all_genres()

    return JSONResponse(content=jsonable_encoder(genre_list), status_code=200)


@router.get('/genre/{id}')
async def get_genre_by_id(genre: RowMapping = Depends(valid_genre_id)) -> JSONResponse:
    return JSONResponse(content=jsonable_encoder(genre), status_code=200)


@router.post('/genre', dependencies=[Depends(valid_creating_genre)])
async def add_genre(genre: GenreCreate) -> Response:
    await service.add_genre(genre.name)

    return Response(status_code=200)


@router.put('/genre', dependencies=[Depends(valid_updating_genre)])
async def update_genre(genre: GenreUpdate) -> Response:
    await service.update_genre(genre.id, genre.name)

    return Response(status_code=200)


@router.delete('/genre', dependencies=[Depends(valid_genre_id)])
async def delete_genre(genre_id: int) -> Response:
    await service.delete_genre(genre_id)

    return Response(status_code=200)
