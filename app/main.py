from fastapi import FastAPI
from app.api.Router import router

app = FastAPI()

app.include_router(router)