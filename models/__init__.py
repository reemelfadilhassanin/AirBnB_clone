#!/usr/bin/python3
"""this module for auto initialize file storage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
import os

storage = FileStorage()
storage.reload()
