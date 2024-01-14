#!/usr/bin/python3
""" City class module"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class City(BaseModel):
	"""City class inhirted from BaseModel class"""
	state_id = ""
	name = ""
