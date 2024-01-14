#!/usr/bin/python3

"""
This storage class for AirBnB to enable persistence
"""

import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage:
    """
    this class enable serializes instances to a JSON file
      and deserializes JSON file to instances
Attributes:
- _file_name (str): the name of the data file
- _users (list): list of users objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name = obj_dict['__class__']
                    cls = BaseModel if class_name == 'BaseModel' else None  # Update with other classes
                    if cls:
                        obj = cls(**obj_dict)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
