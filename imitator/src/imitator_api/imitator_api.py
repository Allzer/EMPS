import os
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from src.imitator_api.imitator_stryctyre import EMPS_STRYCTYRE

router = APIRouter(
    prefix="/imitator_emps",
    tags=["imitator"]
)

# Настраиваем пути к шаблонам
current_dir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(current_dir, "..", "..", "templates")
templates = Jinja2Templates(directory=templates_path)

@router.get('/')
def get_info():
    """API endpoint для получения данных в JSON формате"""
    return EMPS_STRYCTYRE

@router.get('/ui', response_class=HTMLResponse)
async def get_ui(request: Request):
    """Web интерфейс для мониторинга"""
    return templates.TemplateResponse("imitator_ui.html", {"request": request})

@router.post('/refresh')
def refresh_data():
    """Эндпоинт для принудительного обновления данных"""
    return {"status": "data_refreshed", "timestamp": EMPS_STRYCTYRE["timestamp"]}