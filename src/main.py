from fastapi import FastAPI
from bands.router import router as music_router


app: FastAPI = FastAPI(title='Music API')

app.include_router(music_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=4127, reload=True)
