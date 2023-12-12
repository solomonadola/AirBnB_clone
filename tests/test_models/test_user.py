#!/usr/bin/python3
"""Defines unittests for user model.
Unittest classes:
    TestUser_instantiation
    TestUser_save
    TestUser_to_dict
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attribute_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_default_attribute_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        self.user.email = "john@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict(self):
        self.user.email = "john@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        user_dict = self.user.to_dict()

        self.assertEqual(user_dict['email'], "john@example.com")
        self.assertEqual(user_dict['password'], "password123")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertEqual(user_dict['__class__'], "User")
        self.assertIsInstance(user_dict['created_at'], str)
        self.assertIsInstance(user_dict['updated_at'], str)

        created_at = datetime.strptime(user_dict['created_at'],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        updated_at = datetime.strptime(user_dict['updated_at'],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.user.created_at)
        self.assertEqual(updated_at, self.user.updated_at)


if __name__ == '__main__':
    unittest.main()
