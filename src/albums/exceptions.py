from fastapi import HTTPException


class AlbumNotFound(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = 'album not found'


class FailedToCreateAlbum(HTTPException):
    def __init__(self):
        self.status_code = 507
        self.detail = 'failed to insert new album data'


class FailedToUpdateAlbum(HTTPException):
    def __init__(self):
        self.status_code = 500
        self.detail = 'failed to update album data'
