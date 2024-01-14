#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ this model is base for all model in airbnb clone
    it contains the following attributes and methods :
    - id (str): unique identifier of a object instance
    - created_at (datetime): creation date of an
    object instance when the object is
    created. Defaults to current UTC datetime
    - updated_at (datetime): last update date of an object instance.
    """

    def __init__(self, *args, **kwargs):
        """Common default attributes for all instances"""
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """ formating """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        data = {}
        data["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()
            else:
                data[key] = value
        return data
