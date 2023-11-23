from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationshi


class Money(BaseModel):
    """Representation of money"""
    __tablename__ = 'money'
    # financing_options = relationship
    blog = Column(BLOB, nullable=False)
