#!/usr/bin/python3
"""
Unit tests for the User model.
"""
import os
from sqlalchemy import Column
from tests.test_models.test_base_model import TestBasemodel
from models.user import User


class TestUser(TestBasemodel):
    """
    Represents the tests for the User model.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the TestUser class.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name_type(self):
        """
        Tests the type of the 'first_name' attribute.

        Ensures that the 'first_name' attribute of a new User instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.first_name), expected_type)

    def test_last_name_type(self):
        """
        Tests the type of the 'last_name' attribute.

        Ensures that the 'last_name' attribute of a new User instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.last_name), expected_type)

    def test_email_type(self):
        """
        Tests the type of the 'email' attribute.

        Ensures that the 'email' attribute of a new User instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.email), expected_type)

    def test_password_type(self):
        """
        Tests the type of the 'password' attribute.

        Ensures that the 'password' attribute of a new User instance
        has the correct type based on the storage type.
        """
        new = self.value()
        expected_type = str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        self.assertEqual(type(new.password), expected_type)
