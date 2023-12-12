#!/usr/bin/python3
""" This module is a city test module"""
import unittest
from models import base_model
from models.city import City


class TestCity(unittest.TestCase):

    def test_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == '__main__':
    unittest.main()
