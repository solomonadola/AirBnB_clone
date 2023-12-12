#!/usr/bin/python3
""" This module is a state test module"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_attributes(self):
        state = State()
        self.assertEqual(state.name, "")


if __name__ == '__main__':
    unittest.main()
