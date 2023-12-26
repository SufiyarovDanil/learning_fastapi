from fastapi import HTTPException


class GenreNotFound(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = 'genre not found'


class GenreAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = 507
        self.detail = 'genre already exists'
