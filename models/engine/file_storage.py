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
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
