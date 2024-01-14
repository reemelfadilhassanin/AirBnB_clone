#!/usr/bin/python3

"""This storage class for AirBnB to enable persistence
"""

import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

    def all(self, cls=None):
        """ this module for returns the dictionary __objects
        Return:
            returns a dictionary of __object
        """
        return FileStorage.__objects

    def new(self, obj):
        """ this module defines to sets in __objects the
          obj with key <obj class name>.id
        """
        if obj:
            key_object = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key_object] = obj

    def save(self):
        """this module define serialize the file path to JSON file path
        """
        my_dict = {}
        for k, v in self.__objects.items():
            my_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as fil:
            json.dump(my_dict, fil)

    def reload(self):
        """define deserializes the JSON file to __objects (only if the JSON file (__file_path) exists,
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for k, v in (json.load(f)).items():
                    v = eval(v["__class__"])(**v)
                    self.__objects[k] = v
        except FileNotFoundError:
            pass
