#!/usr/bin/python3
"""
models package initialization
"""

from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()

# Import the newly created stats blueprint
from api.v1.views.index import stats

