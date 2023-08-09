from pydantic import BaseModel
from fastapi import HTTPException

class VerificationResponseSchema(BaseModel):
    status_code: int
    detail : bool= None
    error:str = None

class AdminLoginResponse(BaseModel):
    status_code :int
    token:str = None
    error:str = None

class CsvResponseSchema(BaseModel):
    status_code : int
    records_added:int= None
    error:str=None
