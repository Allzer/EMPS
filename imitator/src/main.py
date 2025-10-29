import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from src.imitator_api.imitator_api import router as imitator_router
app = FastAPI()

app.include_router(imitator_router)

# Монтируем статические файлы
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "templates")

if os.path.exists(templates_path):
    app.mount("/static", StaticFiles(directory=templates_path), name="static")

@app.get("/")
def read_root():
    return {"message": "Система мониторинга производства", "version": "1.0"}

from src.imitator_api import imitator_api