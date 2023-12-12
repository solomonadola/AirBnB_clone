#!/usr/bin/python3
""" This module is a city test module"""
import unittest
from models import base_model
from models.city import City


class TestCity(unittest.TestCase):
    def test_city_instance(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, base_model.BaseModel)


if __name__ == '__main__':
    unittest.main()
