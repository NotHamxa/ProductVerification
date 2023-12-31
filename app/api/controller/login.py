from app.api.log.logger import logger,levels
from app.api.auth.auth_handler import signJWT
from app.api.database.db import database
from app.core.Config import AdminLoginSchema
from fastapi import HTTPException
def AuthenticateCredentials(data:AdminLoginSchema):

    state, query = database.checkAdmin(data.Username,data.Password)
    if not state:
        if query == 1:
            logger.log(levels.warning, "Add Product Verification:Admin username does not exist")
        elif query == 2:
            logger.log(levels.warning, f"Add Product Verification:Password for username '{data['Username']}' is incorrect")
        return {"status_code":400,"detail":query}
    return {"status_code":200,"detail":None}