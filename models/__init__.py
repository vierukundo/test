#!/usr/bin/python3
""" Module for managing storage objects """

from models.engine.db_storage import DBStorage
storage = DBStorage()
storage.reload()
