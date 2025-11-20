from fastapi import FastAPI
from src.api.monitoring_api import router as monitoring_router
app = FastAPI()

app.include_router(monitoring_router)

from src.api import monitoring_api