from fastapi import APIRouter,UploadFile,Depends
from fastapi.responses import RedirectResponse
from app.api.auth.auth_bearer import JWTBearer
from app.core.Config import AdminLoginSchema
from app.api.controller.csvHandler import processCsvFile
from app.api.controller.login import AuthenticateCredentials
from app.api.controller.verify import VerifyProduct
from app.core.ResponseSchema import VerificationResponseSchema,AdminLoginResponse,CsvResponseSchema
router = APIRouter()

@router.get("/")
def redirect():
    return RedirectResponse("/docs")

@router.get("/verify/{productId}")
async def verify(productId:str):
    try:
        IsVerified= VerifyProduct(productId)
        if IsVerified==True:
            status_code = 200
        else:
            status_code = 404
        response = VerificationResponseSchema(**{"status_code":status_code,"detail":IsVerified})
        return response

    except Exception as e:
        status_code = 400
        response = VerificationResponseSchema(**{"status_code": status_code,"error":str(e)})
        return response

@router.post("/login/")
async def login(data:AdminLoginSchema):
    try:

        token = AuthenticateCredentials(data)
        status_code = 200
        response = AdminLoginResponse(**{"status_code":status_code,"token":token})
        return response
    except Exception as e:
        status_code = 400
        response = AdminLoginResponse(**{"status_code": status_code, "error": str(e)})
        return response
@router.post("/addproducts/",dependencies=[Depends(JWTBearer())])
async def AddProducts(file:UploadFile):
    try:
        IdsAdded = processCsvFile(file)
        status_code = 200
        response = CsvResponseSchema(**{"status_code":status_code,"records_added":IdsAdded})
        return response
    except Exception as e:
        status_code = 400
        response = CsvResponseSchema(**{"status_code":status_code,"error":str(e)})
        return response


