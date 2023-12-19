from app.models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, BLOB, Boolean, Numeric
from sqlalchemy.orm import relationship


class Machinery(BaseModel, Base):
    """A representation of construction machineries"""
    __tablename__ = 'machineries'
    name = Column(String(128), nullable=False)
    category = Column(String(128), nullable=False)
    picture = Column(String(255), nullable=True, default=None) # store path to picture
    rent = Column(Boolean, default=False)
    price = Column(Numeric(precision=10, scale=2))
    description = Column(String(1024), nullable=False)
    tutorial_video = Column(String(255), nullable=True, default=None) # store path to video that demonstrates how material is used
    vendor = Column(String(255), nullable=True, default=None)
    vendor_email = Column(String(255), nullable=True, default=None)
    vendor_contacts = Column(String(255), nullable=True, default=None)
    vendor_country = Column(String(255), nullable=True, default=None)
