#!/usr/bin/python3
"""this module for auto initialize file storage
"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
