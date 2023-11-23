from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Education(BaseModel, Base):
    """A representation of Education"""
    __tablename__ = 'education'
    institution_name = Column(String(128), nullable=False)
    level_of_education = Column(String(128), nullable=False)
    major = Column(String(128), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    end_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    manpower_id = Column(String(60), ForeignKey('manpowers.id'), nullable=False)
    cv = Column(BLOB)
