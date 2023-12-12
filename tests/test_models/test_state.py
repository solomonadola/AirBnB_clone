#!/usr/bin/python3
""" This module is a state test module"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_state_instance(self):
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()