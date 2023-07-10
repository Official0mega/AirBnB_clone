#!/usr/bin/python3
"""
Unit tests for the State model.
"""
import os

from tests.test_models.test_base_model import TestBasemodel
from models.state import State


class TestState(TestBasemodel):
    """
    Represents the tests for the State model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestState class.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name(self):
        """
        Tests the type of the 'name' attribute.

        Verifies that the 'name' attribute of a State instance is of
        the correct type depending on the storage type (file or database).
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.name), expected_type)
