from pydantic import BaseModel
from fastapi import HTTPException

class VerificationResponseSchema(BaseModel):
    status_code: int
    detail : bool
    error:str = None

class AdminLoginResponse(BaseModel):
    status_code :int
    token:str
    error:str = None

class CsvResponseSchema(BaseModel):
    status_code : int
    records_added:int
    error:str=None
