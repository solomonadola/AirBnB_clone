#!/usr/bin/python3
""" This module is a city test module"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
