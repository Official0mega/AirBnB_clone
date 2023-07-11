#!/usr/bin/python3
"""
Amenity Module for the HBNB project.
"""
import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """
    Represents an amenity data set.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        name (str): The name of the amenity.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
