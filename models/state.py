#!/usr/bin/python3
""" This module is a review module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class."""
    def __init__(self, *args, **kwargs):
        """Initialization of State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
