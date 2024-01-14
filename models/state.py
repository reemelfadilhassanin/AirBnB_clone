#!/usr/bin/python3
""" State class module"""

import uuid
from datetime import datetime
from models import storage
from models.base_model import BaseModel

class State(BaseModel):
	"""State class inhirted from BaseModel class"""
	name = ""
