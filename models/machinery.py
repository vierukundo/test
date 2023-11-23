from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Machinery(BaseModel, Base):
    """A representation of construction machinery"""
    __tablename__ = 'machineries'
    name = Column(String(128), nullable=False)
    picture = Column(BLOB, nullable=False)
    rent = Column(Boolean, default=False)
    price = Column(Numeric(precision=10, scale=2))
    description = Column(String(1024), nullable=False)
    tutorial_video = Column(BLOB)
