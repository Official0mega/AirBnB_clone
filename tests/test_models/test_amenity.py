#!/usr/bin/python3
"""
Unit tests for the Amenity model.
"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.amenity import Amenity


class TestAmenity(TestBasemodel):
    """
    Represents the tests for the Amenity model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestAmenity class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name_type(self):
        """
        Tests the type of the 'name' attribute.

        Verifies that the 'name' attribute of an Amenity instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expected_type)
