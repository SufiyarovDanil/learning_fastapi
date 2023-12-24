from fastapi import HTTPException


class AlbumNotFound(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = 'album not found'
