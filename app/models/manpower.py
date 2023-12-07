from app.models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, LargeBinary
from sqlalchemy.dialects.mysql import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Manpower(BaseModel, Base):
    """Representation of a manpower"""
    __tablename__ = 'manpowers'
    first_name = Column(String(128), nullable=False, default="Olivier")
    last_name = Column(String(128), nullable=False, default="RUKUNDO")
    sex = Column(String(128), nullable=False, default="Male")
    experience = Column(String(128), nullable=False, default="2 years")
    service = Column(String(128), nullable=False, default="Engineer")
    # profile = Column(LONGBLOB)
    profile_path = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, default="vierukundo20@gmail.com")
    contacts = Column(String(128), nullable=False, default="0783464572")
