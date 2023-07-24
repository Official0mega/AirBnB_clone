#!/usr/bin/python3
"""
This module defines a base class for all models in our hbnb clone.

It provides the BaseModel class that serves as the base for all other
model classes. It includes common attributes and methods that are shared
across models.
"""

import os
import uuid
#from tests.test_models.test_base_model import TestBaseModel
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
    A base class for all models in the hbnb clone.

    Attributes:
        id (str): The unique identifier of the model instance.
        created_at (datetime): The datetime when the model instance was created.
        updated_at (datetime): The datetime when the model instance was last updated.
    """

    id = Column(String(60), nullable=False, primary_key=True, unique=True)
    created_at = Column(DATETIME, nullable=False, default=datetime.utcnow())
    updated_at = Column(DATETIME, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If no kwargs are provided, a new BaseModel instance is created
        with a unique id and the current datetime for created_at and updated_at.
        If kwargs are provided, the instance is initialized with the provided
        attributes, and if any of the attributes are missing, they are set to
        default values (id: unique id, created_at/updated_at: current datetime).
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

            if not hasattr(self, 'id'):
                setattr(self, 'id', str(uuid.uuid4()))
            if not hasattr(self, 'created_at'):
                setattr(self, 'created_at', datetime.now())
            if not hasattr(self, 'updated_at'):
                setattr(self, 'updated_at', datetime.now())

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A string representation of the BaseModel instance.
        """
        cls = self.__class__.__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def delete(self):
        """
        Deletes the BaseModel instance from the storage.

        This method removes the current instance from the storage system.
        """
        from models import storage
        storage.delete(self)

    def save(self):
        """
        Saves the BaseModel instance to the storage.

        This method updates the updated_at attribute with the current time,
        adds the instance to the storage system, and saves the changes.
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        res = {}
        for key, value in self.__dict__.items():
            if key != '_sa_instance_state':
                if isinstance(value, datetime):
                    res[key] = value.isoformat()
                else:
                    res[key] = value
        res['__class__'] = self.__class__.__name__
        return res


if __name__ == '__main__':
    import unittest

    class TestBaseModel(unittest.TestCase):
        """
        Test cases for the BaseModel class.
        """

        def test_init(self):
            """Tests the initialization of the BaseModel class."""
            i = BaseModel()
            self.assertIsInstance(i, BaseModel)

        def test_id(self):
            """Tests the type of id."""
            new = BaseModel()
            self.assertEqual(type(new.id), str)

        def test_created_at(self):
            """Tests the type of created_at."""
            new = BaseModel()
            self.assertEqual(type(new.created_at), datetime)

        def test_updated_at(self):
            """Tests the type of updated_at."""
            new = BaseModel()
            self.assertEqual(type(new.updated_at), datetime)

        def test_str(self):
            """Tests the __str__ function of the BaseModel class."""
            i = BaseModel()
            self.assertEqual(str(i), '[BaseModel] ({}) {}'.format(i.id, i.__dict__))

        def test_save(self):
            """Tests the save function of the BaseModel class."""
            i = BaseModel()
            i.save()
            self.assertIsNotNone(i.updated_at)

        def test_to_dict(self):
            """Tests the to_dict function of the BaseModel class."""
            i = BaseModel()
            d = i.to_dict()
            self.assertEqual(type(d), dict)
            self.assertIn('__class__', d)
            self.assertIn('id', d)
            self.assertIn('created_at', d)
            self.assertIn('updated_at', d)

    unittest.main()
