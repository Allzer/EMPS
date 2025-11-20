import json
from fastapi import APIRouter, Request
from sqlalchemy import select

from database import SessionDep
from src.models.monitoring_models import SystemsModel
from src.api.scripts import check_system, create_system

router = APIRouter(
    prefix="/monitoring",
    tags=["monitoring"]
)

@router.get('/')
async def get_info(request: Request):
    """Главная страница с данными и формами"""
    return 'monitoring'

@router.post('/')
async def post_ftp_data(request: Request):
    data = await request.json()
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    
    return 'ok'

@router.post('/create_system')
async def post_ftp_data(request: Request, session : SessionDep):
    data = await request.json()

    
    system_id = await check_system(data)

    system = select(SystemsModel).where(SystemsModel.id == system_id)
    query = await session.execute(system)
    query = query.scalars().first()

    return {
        'system_name': query.system_name,
        'system_key': query.system_key,
        'list_of_sensors': {}
    }