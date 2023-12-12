#!/usr/bin/python3
""" This module is a place test module"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_place_instance(self):
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
