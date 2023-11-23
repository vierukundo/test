#!/usr/bin/python3
"""Definition of BaseModel class"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """BaseModel class representation"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], date_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], date_format)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
    
    def save(self):
        """
        updates attribute updated_at - with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
    
    def to_dict(self):
        """
        This Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        objects = self.__dict__.copy()
        objects["created_at"] = self.created_at.isoformat()
        objects["updated_at"] = self.updated_at.isoformat()
        objects["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in objects:
            del objects["_sa_instance_state"]

        return objects
    
    def __str__(self):
        """
        Return the string representation of this class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
