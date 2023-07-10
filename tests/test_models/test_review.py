#!/usr/bin/python3
"""
Unit tests for the Review model.
"""
import os
from tests.test_models.test_base_model import TestBasemodel
from models.review import Review


class TestReview(TestBasemodel):
    """
    Unit tests for the Review model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestReview class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id_type(self):
        """
        Tests the type of the 'place_id' attribute.

        Ensures that the 'place_id' attribute of a new Review instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.place_id), expected_type)

    def test_user_id_type(self):
        """
        Tests the type of the 'user_id' attribute.

        Ensures that the 'user_id' attribute of a new Review instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.user_id), expected_type)

    def test_text_type(self):
        """
        Tests the type of the 'text' attribute.

        Ensures that the 'text' attribute of a new Review instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.text), expected_type)
