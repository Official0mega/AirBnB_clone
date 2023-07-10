#!/usr/bin/python3
"""
Module for testing file storage.
"""
import os
import unittest

from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') == 'db', 'FileStorage test')
class TestFileStorage(unittest.TestCase):
    """
    Class to test the file storage method.

    Methods:
        test_obj_list_empty: Test that __objects is initially empty.
        test_new: Test that a new object is correctly added to __objects.
        test_all: Test that __objects is properly returned.
        test_base_model_instantiation: Test that a file is not created on BaseModel save.
        test_empty: Test that data is saved to the file.
        test_save: Test the FileStorage save method.
        test_reload: Test that the storage file is successfully loaded to __objects.
        test_reload_empty: Test loading from an empty file.
        test_reload_from_nonexistent: Test that nothing happens if the file does not exist.
        test_base_model_save: Test that the BaseModel save method calls the storage save.
        test_type_path: Test that __file_path is a string.
        test_type_objects: Test that __objects is a dictionary.
        test_key_format: Test that the key is properly formatted.
        test_storage_var_created: Test that the FileStorage object storage is created.
    """

    def setUp(self):
        """
        Set up the test environment.
        """
        # Clear the objects in storage
        storage._FileStorage__objects = {}

    def tearDown(self):
        """
        Clean up after each test.
        """
        # Remove the storage file
        try:
            os.remove('file.json')
        except FileNotFoundError:
            pass

    def test_obj_list_empty(self):
        """
        Test that __objects is initially empty.
        """
        self.assertEqual(len(storage.all()), 0)

    def test_new(self):
        """
        Test that a new object is correctly added to __objects.
        """
        new = BaseModel()
        new.save()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)

    def test_all(self):
        """
        Test that __objects is properly returned.
        """
        new = BaseModel()
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_instantiation(self):
        """
        Test that a file is not created on BaseModel save.
        """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))

    def test_empty(self):
        """
        Test that data is saved to the file.
        """
        new = BaseModel()
        thing = new.to_dict()
        new.save()
        new2 = BaseModel(**thing)
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_save(self):
        """
        Test the FileStorage save method.
        """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """
        Test that the storage file is successfully loaded to __objects.
        """
        new = BaseModel()
        new.save()
        storage.reload()
        loaded = None
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_empty(self):
        """
        Test loading from an empty file.
        """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """
        Test that nothing happens if the file does not exist.
        """
        self.assertIsNone(storage.reload())

    def test_base_model_save(self):
        """
        Test that the BaseModel save method calls the storage save.
        """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_type_path(self):
        """
        Test that __file_path is a string.
        """
        self.assertEqual(type(storage._FileStorage__file_path), str)

    def test_type_objects(self):
        """
        Test that __objects is a dictionary.
        """
        self.assertEqual(type(storage.all()), dict)

    def test_key_format(self):
        """
        Test that the key is properly formatted.
        """
        new = BaseModel()
        _id = new.to_dict()['id']
        temp = ''
        new.save()
        for key, value in storage.all().items():
            if value is new:
                temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    def test_storage_var_created(self):
        """
        Test that the FileStorage object storage is created.
        """
        self.assertEqual(type(storage), FileStorage)


if __name__ == '__main__':
    unittest.main()
