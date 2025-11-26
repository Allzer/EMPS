import json
from fastapi import APIRouter, Request
from sqlalchemy import select

from database import SessionDep
from src.models.monitoring_models import SensorsModel, SystemsModel
from src.api.scripts import add_sensor, add_states, check_system

router = APIRouter(
    prefix="/monitoring",
    tags=["monitoring"]
)

@router.get('/')
async def get_info(request: Request):
    """Главная страница с данными и формами"""
    return 'monitoring'

@router.post('/create_system')
async def create_system(request: Request, session : SessionDep):
    data = await request.json()

    system_id = await check_system(data)

    system = select(SystemsModel).where(SystemsModel.id == system_id)
    query = await session.execute(system)
    query = query.scalars().first()

    sensors = (select(SensorsModel)).where(SensorsModel.system_id == system_id)
    sensors_query = await session.execute(sensors)
    sensors_info = sensors_query.scalars().all()

    result_dict = {}
    for sensor in sensors_info:
        result_dict.update(
            {
                sensor.sensor_name: sensor.id
            }
        )

    return {
        'system_id': system_id,
        'system_name': query.system_name,
        'system_key': query.system_key,
        'list_of_sensors': result_dict
    }


@router.post('/add_sensors')
async def add_sensors_info(request: Request):
    data = await request.json()
    await add_sensor(data)
    return 'Сенсоры обновлены или добавлены'

@router.post('/add_sensor_states')
async def add_sensor_states(request: Request):
    data = await request.json()
    await add_states(data)
    return 'Состояния добавлены'
