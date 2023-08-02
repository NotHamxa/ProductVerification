from app.api.database.db import database

def VerifyProduct(productId):
    response = database.read({"VerificationCode":productId})
    if response==None:
        return {"status":200,"detail":False}
    else:
        return {"status":200,"detail":True}
