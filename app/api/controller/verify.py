from app.api.database.db import database

def VerifyProduct(productId):
    response = database.read({"VerificationCode":productId})
    if response==None:
        return False
    else:
        return True
