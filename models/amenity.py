#!/usr/bin/python3

""" Amenity Class module
this class inhirted from BaseModel module
to create a new new amenity objects
while inheriting all properties of baseModel
"""


from models.base_model import BaseModel


class Amenity(BaseModel):
	"""Amenity class inhirted from BaseModel class
	with one public attribute name as an empty str
	"""
	name = ""
