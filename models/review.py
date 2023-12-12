#!/usr/bin/python3
""" This module is a review module"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class that inherits from BaseModel."""
    place_id = ""
    user_id = ""
    text = ""
