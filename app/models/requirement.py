from app.models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Requirement(BaseModel, Base):
    """Representation of opportunity requirements"""
    __tablename__ = 'requirements'
    name = Column(String(128), nullable=False)
    opportunity_id = Column(String(60), ForeignKey('opportunities.id'), nullable=False)
