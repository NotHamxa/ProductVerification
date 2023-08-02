import time
from typing import Dict
import jwt
from decouple import config


JWT_SECRET ='588667cac472034545a7fb86eed81e955e5cb53ded3e1c40'
JWT_ALGORITHM = "HS256"


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