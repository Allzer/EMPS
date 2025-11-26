import uuid

from sqlalchemy import select
from database import async_session_maker
from src.models.monitoring_models import SensorsModel, SensorsStateModel, SystemsModel

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
        for sensor_device in data:
            sensor = select(SensorsModel).where(SensorsModel.sensor_name == sensor_device['sensor_name'])
            query = await session.execute(sensor)
            query = query.scalars().first()
            
            if not query:
                id_sensors = uuid.uuid4()

                sensors = SensorsModel(
                    id = id_sensors,
                    system_id = sensor_device['system_id'],
                    sensor_name = sensor_device['sensor_name'],
                )

                session.add(sensors)
                await session.commit()

async def add_states(data):
    async with async_session_maker() as session:
        for sensor_states in data:
            sensor = select(SensorsModel).where(SensorsModel.sensor_name == sensor_states['device_name'])
            query = await session.execute(sensor)
            query = query.scalars().first()

            if not query:
                id_sensors_states = uuid.uuid4()

                sensor_description = sensor_states.get('description')
                sensors_states = SensorsStateModel(
                    id = id_sensors_states,
                    sensor_id = query.id,
                    state = sensor_states['device_state'],
                    description = sensor_description,
                )

                session.add(sensors_states)
                await session.commit()
