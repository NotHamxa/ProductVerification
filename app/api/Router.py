from fastapi import APIRouter,UploadFile,Depends
from fastapi.responses import RedirectResponse
from app.api.auth.auth_bearer import JWTBearer
from app.core.Config import AdminLoginSchema
from app.api.controller.csvHandler import processCsvFile
from app.api.controller.login import AuthenticateCredentials
from app.api.controller.verify import VerifyProduct

router = APIRouter()

@router.get("/")
def redirect():
    return RedirectResponse("/docs")

@router.get("/verify/{productId}")
async def verify(productId:str):
    try:

        return VerifyProduct(productId)
    except Exception as e:
        return e


@router.post("/login/")
async def login(data:AdminLoginSchema):
    try:
        return AuthenticateCredentials(data)
    except Exception as e:
        return e
@router.post("/addproducts/",dependencies=[Depends(JWTBearer())])
async def AddProducts(file:UploadFile):
    try:
        return processCsvFile(file)
    except Exception as e:
        return e

