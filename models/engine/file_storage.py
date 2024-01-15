#!/usr/bin/python3

"""This storage class for AirBnB to enable persistence
"""
import os
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

    def classes(self):
        """match the classe"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """this to generate objects using deserlize"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
            obj_dict = json.load(f)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict

    def attributes(self):
        """check the valid attributes"""
        attributes = {
            "BaseModel":
            {"id": str,
             "created_at": datetime.datetime,
             "updated_at": datetime.datetime},
                "User":
            {"email": str,
             "password": str,
             "first_name": str,
             "last_name": str},
                "State":
            {"name": str},
                "City":
            {"state_id": str,
             "name": str},
                "Amenity":
            {"name": str},
                "Place":
            {"city_id": str,
             "user_id": str,
             "name": str,
             "description": str,
             "number_rooms": int,
             "number_bathrooms": int,
             "max_guest": int,
             "price_by_night": int,
             "latitude": float,
             "longitude": float,
             "amenity_ids": list},
                "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
