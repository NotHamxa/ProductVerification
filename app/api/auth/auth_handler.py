import time
from typing import Dict
import jwt
from decouple import config
from app.core.Config import settings

JWT_SECRET =settings.JWT_SECRET
JWT_ALGORITHM = settings.JWT_ALGORITHM


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(userId:str):
    payload={
        "userId":userId,
        "expires":time.time() + 600
    }
    token = jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)

def decodeJWT(token:str):
    try:
        decodedToken = jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
        return decodedToken if decodedToken["expires"] >=time.time() else None
    except:
        return {}