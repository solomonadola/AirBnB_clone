#!/usr/bin/python3
""" This module is a amenity test module"""

import unittest
from models import base_model
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_amenity_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, base_model.BaseModel)


if __name__ == '__main__':
    unittest.main()
