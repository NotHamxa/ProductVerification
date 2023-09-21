from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.Router import router
from app.core.Config import settings


origins = settings.origins.split(",")
app = FastAPI(title="Product Verification API")
app.add_middleware(CORSMiddleware,
                   allow_origins = origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])


app.include_router(router)