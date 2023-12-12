#!/usr/bin/python3
""" This module is a amenity test module"""

import unittest
from models import base_model
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def test_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
