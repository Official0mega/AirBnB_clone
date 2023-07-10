#!/usr/bin/python3
"""
Unit tests for the City model.
"""
import os

from models.city import City
from tests.test_models.test_base_model import TestBasemodel


class TestCity(TestBasemodel):
    """
    Represents the tests for the City model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestCity class.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Tests the type of the 'state_id' attribute.

        Verifies that the 'state_id' attribute of a City instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.state_id), expected_type)

    def test_name(self):
        """
        Tests the type of the 'name' attribute.

        Verifies that the 'name' attribute of a City instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expected_type)
