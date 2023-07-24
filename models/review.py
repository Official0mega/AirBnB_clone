#!/usr/bin/python3
"""
Review module for the HBNB project.

This module defines the Review class, which represents review information
for places in the HBNB project. It inherits from the BaseModel class and
the Base class for database storage.
"""

import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Review class to store review information.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        place_id (str): The place ID associated with the review.
        user_id (str): The user ID associated with the review.
        text (str): The text content of the review.
    """

    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    text = Column(String(1024), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else''
