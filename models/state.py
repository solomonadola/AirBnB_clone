#!/usr/bin/python3
""" This module is a review module"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class that inherits from BaseModel."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
