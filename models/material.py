from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, BLOB, Boolean, Numeric
from sqlalchemy.orm import relationship


class Material(BaseModel, Base):
    """A representation of construction material"""
    __tablename__ = 'materials'
    name = Column(String(128), nullable=False)
    picture = Column(BLOB, nullable=False)
    rent = Column(Boolean, default=False)
    price = Column(Numeric(precision=10, scale=2))
    description = Column(String(1024), nullable=False)
    tutorial_video = Column(BLOB)
    # locations = relationship("Location", backref="material", cascade="delete")
