import uuid

from sqlalchemy import select
from database import async_session_maker
from src.models.monitoring_models import SensorsModel, SystemsModel

async def check_system(data):
    async with async_session_maker() as session:
        system = select(SystemsModel).where(SystemsModel.system_name == data['system_name'])
        query = await session.execute(system)
        query = query.scalars().first()
        
        if not query:
            system_id = await create_system(data)
        else:
            system_id = query.id
        return system_id

async def create_system(data):
    async with async_session_maker() as session:
        id_system = uuid.uuid4()

        systems = SystemsModel(
            id = id_system,
            system_name = data['system_name'],
            system_key = data['system_key'],
        )

        session.add(systems)
        await session.commit()
    return id_system

async def add_sensor(data):
    async with async_session_maker() as session:
        for sensor in data:
            id_sensors = uuid.uuid4()

            sensors = SensorsModel(
                id = id_sensors,
                system_id = sensor['system_id'],
                sensor_name = sensor['sensor_name'],
            )

            session.add(sensors)
        await session.commit()