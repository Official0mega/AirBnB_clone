#!/usr/bin/python3
"""
City Module for the HBNB project.
"""
import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    Represents a city in the HBNB project.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        name (str): The name of the city.
        state_id (str): The ID of the state associated with the city.
        places (relationship): The places associated with the city.
    """
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship('Place', cascade='all, delete, delete-orphan', backref='cities') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
