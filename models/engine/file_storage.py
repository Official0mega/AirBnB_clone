#!/usr/bin/python3
"""
This module defines a class to manage file storage for the hbnb clone.
"""
import json
import os
from importlib import import_module


class FileStorage:
    """
    This class manages the storage of hbnb models in JSON format.
    """

    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Initializes a FileStorage instance."""
        self.model_classes = {
            'BaseModel': import_module('models.base_model').BaseModel,
            'User': import_module('models.user').User,
            'State': import_module('models.state').State,
            'City': import_module('models.city').City,
            'Amenity': import_module('models.amenity').Amenity,
            'Place': import_module('models.place').Place,
            'Review': import_module('models.review').Review
        }

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage.

        Args:
            cls (class, optional): The class to filter the objects. Defaults to None.

        Returns:
            dict: A dictionary of objects in storage.
        """
        if cls is None:
            return FileStorage.__objects
        # Access the class-level attribute correctly
        else:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                if isinstance(value, cls):
                    filtered_dict[key] = value
            return filtered_dict

    def delete(self, obj=None):
        """
        Removes an object from the storage dictionary.

        Args:
            obj (BaseModel, optional): The object to delete. Defaults to None.
        """
        if obj is not None:
            obj_key = obj.to_dict()['__class__'] + '.' + obj.id
            if obj_key in self.__objects.keys():
                del self.__objects[obj_key]

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.

        Args:
            obj (BaseModel): The object to add.
        """
        obj_key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[obj_key] = obj

    def save(self):
        """Saves the storage dictionary to a file."""
        with open(self.__file_path, 'w') as file:
            temp = {}
            for key, val in self.__objects.items():
                temp[key] = val.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Loads the storage dictionary from a file."""
        classes = self.model_classes
        if os.path.isfile(self.__file_path):
            temp = {}
            with open(self.__file_path, 'r') as file:
                temp = json.load(file)
                for key, val in temp.items():
                    obj_class = val['__class__']
                    if obj_class in classes:
                        self.__objects[key] = classes[obj_class](**val)

    def close(self):
        """Closes the storage engine."""
        self.reload()
