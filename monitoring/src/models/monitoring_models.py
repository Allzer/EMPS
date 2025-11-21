from sqlalchemy import INTEGER, Column, ForeignKey, Uuid, TEXT

from database import Base

__all__ = [
    'SystemsModel'
]

class SystemsModel(Base):

    __tablename__ = 'systems'

    id = Column(Uuid, primary_key=True)
    
    system_name = Column(TEXT, nullable=False)
    system_key = Column(TEXT, nullable=False, unique=True)


class SensorsModel(Base):

    __tablename__ = 'sensors'

    id = Column(Uuid, primary_key=True)
    system_id = Column(Uuid, ForeignKey('systems.id'))

    sensor_name = Column(TEXT, nullable=False)
    state = Column(INTEGER, nullable=False)
    description = Column(INTEGER, nullable=False)