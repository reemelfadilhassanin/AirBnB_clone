#!/usr/bin/python3
"""This storage class for AirBnB to enable persistence"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from uuid import uuid4
from datetime import datetime
import models


class FileStorage:
    """this class enable serializes instances to a JSON file
      and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
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
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_dict = {'BaseModel': BaseModel, 'User': User}
                    obj_instance = class_dict[class_name](**value)
                    FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
