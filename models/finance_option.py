from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, BLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class FinanceOption(BaseModel, Base):
    """Representation of financing option"""
    __tablename__ = 'finance_options'
    program_name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    photo = Column(BLOB, nullable=False)
    money_id = Column(String(60), ForeignKey('money.id'), nullable=False)
