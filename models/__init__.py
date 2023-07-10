#!/usr/bin/python3
"""
This module instantiates an object of class FileStorage or DBStorage
based on the HBNB_TYPE_STORAGE environment variable.
"""
import os

from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Instantiate a FileStorage or DBStorage object based on HBNB_TYPE_STORAGE
storage = DBStorage() if os.getenv('HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""
A unique FileStorage/DBStorage instance for all models.
"""

# Reload the storage data
storage.reload()
