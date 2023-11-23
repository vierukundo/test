#!/usr/bin/python3
""" Module for managing storage objects """
from models import manpower
from models import base_model
from models import material
from models import machinery
from models import location
from models import opportunity
from models import requirement
from models import money

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()

__all__ = ["manpower", "base_model", "material", "machinery", "storage", "opportunity", "money", "requirement", "location"]
