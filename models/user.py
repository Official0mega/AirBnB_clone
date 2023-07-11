#!/usr/bin/python3
"""
This module defines a class User.
"""
import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    User class to store user information.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        places (relationship): A relationship to the Place class.
        reviews (relationship): A relationship to the Review class.
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    password = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    first_name = Column(String(128), nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    last_name = Column(String(128), nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    places = relationship('Place', cascade="all, delete, delete-orphan", backref='user') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    reviews = relationship('Review', cascade="all, delete, delete-orphan", backref='user') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
