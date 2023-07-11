#!/usr/bin/python3
"""
Place Module for the HBNB project.
"""
import os
from tests.test_models.test_base_model import TestBaseModel
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        nullable=False,
        primary_key=True
    ),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        nullable=False,
        primary_key=True
    )
)
"""
Represents the many-to-many relationship table
between Place and Amenity records.
"""


class Place(BaseModel, Base):
    """
    A class representing a place to stay in the HBNB project.

    Attributes:
        __tablename__ (str): The table name for the database storage.
        city_id (str): The ID of the city associated with the place.
        user_id (str): The ID of the user associated with the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests allowed in the place.
        price_by_night (int): The price per night for the place.
        latitude (float): The latitude coordinate of the place.
        longitude (float): The longitude coordinate of the place.
        amenity_ids (list): The IDs of the amenities associated with the place.
        reviews (relationship): The reviews associated with the place.
        amenities (property): The amenities of the place.
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(String(128), nullable=False) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(String(1024), nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(Integer, nullable=False, default=0) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    number_bathrooms = Column(Integer, nullable=False, default=0) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    max_guest = Column(Integer, nullable=False, default=0) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    price_by_night = Column(Integer, nullable=False, default=0) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0
    latitude = Column(Float, nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    longitude = Column(Float, nullable=True) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else 0.0
    amenity_ids = []
    reviews = relationship('Review', cascade='all, delete, delete-orphan', backref='place') if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship('Amenity', secondary=place_amenity, viewonly=False, backref='place_amenities')
    else:
        @property
        def amenities(self):
            """Returns the amenities of this Place"""
            from models import storage
            amenities_of_place = []
            for value in storage.all(Amenity).values():
                if value.id in self.amenity_ids:
                    amenities_of_place.append(value)
            return amenities_of_place

        @amenities.setter
        def amenities(self, value):
            """Adds an amenity to this Place"""
            if isinstance(value, Amenity):
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Returns the reviews of this Place"""
            from models import storage
            reviews_of_place = []
            for value in storage.all(Review).values():
                if value.place_id == self.id:
                    reviews_of_place.append(value)
            return reviews_of_place
