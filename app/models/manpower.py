from app.models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, Float
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Manpower(BaseModel, Base):
    """Representation of a manpower"""
    __tablename__ = 'manpowers'
    first_name = Column(String(128), nullable=False, default=None)
    last_name = Column(String(128), nullable=False, default=None)
    sex = Column(String(128), nullable=False, default=None)
    experience = Column(String(128), nullable=False, default=None)
    profession = Column(String(128), nullable=False, default=None)
    profile = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, default=None)
    contacts = Column(String(128), nullable=False, default=None)
    country = Column(String(128), nullable=False, default=None)
    city = Column(String(128), nullable=False, default=None)
    date_of_birth = Column(String(128), nullable=False, default=None)
    cv = Column(String(128), nullable=False, default=None)
    wage_per_hour = Column(String(128), nullable=False, default=None)
