#!/usr/bin/python3
"""
Unit tests for the Place model.
"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """
    Represents the tests for the Place model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestPlace class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Tests the type of the 'city_id' attribute.

        Verifies that the 'city_id' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.city_id), expected_type)

    def test_user_id(self):
        """
        Tests the type of the 'user_id' attribute.

        Verifies that the 'user_id' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.user_id), expected_type)

    def test_name(self):
        """
        Tests the type of the 'name' attribute.

        Verifies that the 'name' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expected_type)

    def test_description(self):
        """
        Tests the type of the 'description' attribute.

        Verifies that the 'description' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.description), expected_type)

    def test_number_rooms(self):
        """
        Tests the type of the 'number_rooms' attribute.

        Verifies that the 'number_rooms' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.number_rooms), expected_type)

    def test_number_bathrooms(self):
        """
        Tests the type of the 'number_bathrooms' attribute.

        Verifies that the 'number_bathrooms' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.number_bathrooms), expected_type)

    def test_max_guest(self):
        """
        Tests the type of the 'max_guest' attribute.

        Verifies that the 'max_guest' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.max_guest), expected_type)

    def test_price_by_night(self):
        """
        Tests the type of the 'price_by_night' attribute.

        Verifies that the 'price_by_night' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.price_by_night), expected_type)

    def test_latitude(self):
        """
        Tests the type of the 'latitude' attribute.

        Verifies that the 'latitude' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.latitude), expected_type)

    def test_longitude(self):
        """
        Tests the type of the 'longitude' attribute.

        Verifies that the 'longitude' attribute of a Place instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.longitude), expected_type)

    def test_amenity_ids(self):
        """
        Tests the type of the 'amenity_ids' attribute.

        Verifies that the 'amenity_ids' attribute of a Place instance is a list.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
