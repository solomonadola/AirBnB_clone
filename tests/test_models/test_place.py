#!/usr/bin/python3
""" This module is a place test module"""
import unittest
from models import base_model
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, base_model.BaseModel)


if __name__ == '__main__':
    unittest.main()
