#!/usr/bin/python3
""" __init__ a magic method for models package """

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
