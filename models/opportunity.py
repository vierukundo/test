from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Opportunity(BaseModel, Base):
    """Representation of opportunity. It can be a job, internship, Trainings or Education"""
    __tablename__ = 'opportunities'
    title = Column(String(128), nullable=False)
    employer = Column(String(128), nullable=False)
    # location = 
    type = Column(String(128), nullable=False, default='Job')
    # requirements = relationship
    remote = Column(Boolean, default=False)
