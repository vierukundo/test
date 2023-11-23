from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Manpower(BaseModel, Base):
    """Representation of a manpower"""
    __tablename__ = 'manpowers'
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    sex = Column(String(128), nullable=False)
    experience = Column(String(128), nullable=False)
    service = Column(String(128), nullable=False)
    profile = Column(BLOB, nullable=False)
    email = Column(String(128), nullable=False)
    contacts = Column(String(128), nullable=False)
