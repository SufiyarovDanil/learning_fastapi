from fastapi import FastAPI
from bands.router import router as music_router
from albums.router import router as album_router
from genres.router import router as genre_router


app: FastAPI = FastAPI(title='Music API')

app.include_router(music_router)
app.include_router(album_router)
app.include_router(genre_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('__main__:app', host='127.0.0.1', port=4127, reload=True)
