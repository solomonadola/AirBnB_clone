#!/usr/bin/python3
""" This module is a Amenity module"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""
    def __init__(self, *args, **kwargs):
        """Initialization of Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
