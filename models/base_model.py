#!/usr/bin/python3
"""Definition of BaseModel class"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """BaseModel class representation"""
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
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        This Method returns a dictionary containing all
        keys/values of __dict__ instance
        """
        objects = self.__dict__.copy()
        objects["created_at"] = self.created_at.isoformat()
        objects["updated_at"] = self.updated_at.isoformat()
        objects["__class__"] = self.__class__.__name__

        return objects
    
    def __str__(self):
        """
        Return the string representation of this class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)