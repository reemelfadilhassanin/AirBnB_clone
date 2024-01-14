#!/usr/bin/python3
""" Amenity class module"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class Amenity(BaseModel):
	"""Amenity class inhirted from BaseModel class"""
	name = ""
