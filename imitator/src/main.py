from fastapi import FastAPI
from src.imitator_api.imitator_api import router as imitator_router
app = FastAPI()

app.include_router(imitator_router)

from src.imitator_api import imitator_api