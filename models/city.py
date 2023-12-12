#!/usr/bin/python3
""" This module is a city module"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
