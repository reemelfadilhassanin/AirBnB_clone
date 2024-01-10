#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""

from uuid import uuid4
from datetime import datetime

class BaseModel:
	def __init__(self):
		"""Common default attributes for all instances"""
		self.id = str(uuid4())
		self.created_at = datetime.now()
		self.updates_at = datetime.now()
	def __str__(self):
		""" formating """
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		"""updates the public instance attribute updated_at"""
		self.updates_at = datetime.now()

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
