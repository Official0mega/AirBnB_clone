#!/usr/bin/python3
"""
State Module for the HBNB project.
"""
import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """
    A class representing a state in the HBNB project.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        name (str): The name of the state.
        cities (relationship): The cities associated with the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', cascade='all, delete, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_in_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
