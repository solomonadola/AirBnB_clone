#!/usr/bin/python3
"""
user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """ User a subclass of BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
