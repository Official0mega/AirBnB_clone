#!/usr/bin/python3
"""
Unit tests for the BaseModel.
"""
from datetime import datetime
import json
import os
import unittest

from models.base_model import BaseModel, Base


class TestBaseModel(unittest.TestCase):
    """
    Represents the tests for the BaseModel class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the test class.
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Performs some operations before the tests are run.
        """
        pass

    def tearDown(self):
        """
        Performs some operations after the tests are run.
        """
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_init(self):
        """
        Tests the initialization of the BaseModel class.

        Ensures that the BaseModel class is correctly initialized and
        instances of BaseModel are of the correct type.
        """
        instance = self.value()
        self.assertIsInstance(instance, BaseModel)
        if self.value is not BaseModel:
            self.assertIsInstance(instance, Base)
        else:
            self.assertNotIsInstance(instance, Base)

    def test_default(self):
        """
        Tests the default value stored in BaseModel instances.

        Verifies that the value stored in instances of BaseModel is of
        the correct type.
        """
        instance = self.value()
        self.assertEqual(type(instance), self.value)

    def test_kwargs(self):
        """
        Tests the usage of kwargs during object creation.

        Verifies that instances of BaseModel can be created using keyword
        arguments (kwargs) and the resulting object is not the same as the
        original instance.
        """
        instance = self.value()
        copy = instance.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is instance)

    def test_kwargs_int(self):
        """
        Tests the usage of kwargs with an integer.

        Ensures that passing an integer as a key in kwargs raises a TypeError
        since the BaseModel class only accepts string keys.
        """
        instance = self.value()
        copy = instance.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
    def test_save(self):
        """
        Tests the save function of the BaseModel class.

        Verifies that calling the save method on a BaseModel instance saves
        the instance's data to the appropriate storage (file or database).
        """
        instance = self.value()
        instance.save()
        key = f'{self.name}.{instance.id}'
        with open('file.json', 'r') as f:
            data = json.load(f)
            self.assertEqual(data[key], instance.to_dict())

    def test_str(self):
        """
        Tests the __str__ function of the BaseModel class.

        Ensures that the __str__ function returns the expected string
        representation of a BaseModel instance.
        """
        instance = self.value()
        expected_str = f'[{self.name}] ({instance.id}) {instance.__dict__}'
        self.assertEqual(str(instance), expected_str)

    def test_todict(self):
        """
        Tests the to_dict function of the BaseModel class.

        Verifies that the to_dict method returns a dictionary representation
        of a BaseModel instance with the correct keys and values.
        """
        instance = self.value()
        dict_data = instance.to_dict()
        self.assertEqual(instance.to_dict(), dict_data)
        self.assertIsInstance(dict_data, dict)
        self.assertIn('id', dict_data)
        self.assertIn('created_at', dict_data)
        self.assertIn('updated_at', dict_data)
        self.assertIsInstance(dict_data['created_at'], str)
        self.assertIsInstance(dict_data['updated_at'], str)
        datetime_now = datetime.today()
        instance.id = '012345'
        instance.created_at = instance.updated_at = datetime_now
        expected_dict = {
            'id': '012345',
            '__class__': instance.__class__.__name__,
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(instance.to_dict(), expected_dict)

    def test_delete(self):
        """
        Tests the delete function of the BaseModel class.

        Verifies that calling the delete method on a BaseModel instance removes
        the instance from the storage (file or database).
        """
        instance = self.value()
        instance.save()
        self.assertTrue(instance in instance._BaseModel__objects.values())
        instance.delete()
        self.assertFalse(instance in instance._BaseModel__objects.values())
