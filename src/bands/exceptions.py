from fastapi import HTTPException


class BandNotFound(HTTPException):
    def __init__(self):
        self.status_code = 404
        self.detail = 'band not found'


class BandAlreadyExists(HTTPException):
    def __init__(self):
        self.status_code = 507
        self.detail = 'band already exists'
