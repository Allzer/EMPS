from sqlalchemy import Column, Uuid, TEXT

from database import Base

__all__ = [
    'SystemsModel'
]

class SystemsModel(Base):

    __tablename__ = 'systems'

    id = Column(Uuid, primary_key=True)
    
    system_name = Column(TEXT, nullable=False)
    system_key = Column(TEXT, nullable=False)