#!/usr/bin/python3
"""
Initialization file for the application.
This file sets up the storage engine and loads any existing data 
from the storage file.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
