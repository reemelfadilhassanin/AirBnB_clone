#!/usr/bin/python3
"""this module for auto initialize file storage
"""


from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
