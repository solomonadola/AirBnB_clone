#!/usr/bin/python3
""" This module is a amenity test module"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)


if __name__ == '__main__':
    unittest.main()
