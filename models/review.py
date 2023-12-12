#!/usr/bin/python3
""" This module is a review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""
    def __init__(self, *args, **kwargs):
        """Initialization of Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
