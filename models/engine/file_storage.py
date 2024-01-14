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

    def __init__(self):
        pass

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized = {
            key: val.to_dict()
            for key, val in self.__objects.items()
        }
        with open(FileStorage.__file_path, "w") as f:
            f.write(json.dumps(serialized))

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            deserialized = {}
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.loads(f.read())
            FileStorage.__objects = {
                key:
                    eval(obj["__class__"])(**obj)
                    for key, obj in deserialized.items()}
        except FileNotFoundError:
            pass
