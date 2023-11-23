from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Location(BaseModel, Base):
    """Representation of Location"""
    __tablename__ = 'locations'
    country = Column(String(128), nullable=False)
    city = Column(String(128), nullable=False)
    state = Column(String(128))
    address = Column(String(128))
    material_id = Column(String(60), ForeignKey('materials.id'), nullable=False)
    machinery_id = Column(String(60), ForeignKey('machineries.id'), nullable=False)
    opportunity_id = Column(String(60), ForeignKey('opportunities.id'), nullable=False)
