#!/usr/bin/python3
"""
This module handles all tests related to BaseModel class
"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setting up TestBaseModel class...')

    @classmethod
    def tearDownClass(cls):
        print('Tearing down TestBaseModel class...')

    def setUp(self):
        print('Setting up a test...')
        self.base_model = BaseModel()

    def tearDown(self):
        print('Tearing down a test...')

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_method(self):
        with patch('models.storage.save') as mock_save:
            self.base_model.save()
            mock_save.assert_called_once()

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'],
                         self.base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_str_method(self):
        str_representation = str(self.base_model)
        self.assertIn('BaseModel', str_representation)
        self.assertIn(self.base_model.id, str_representation)
        self.assertIn(str(self.base_model.__dict__), str_representation)

    def test_init_method_with_arguments(self):
        new_model = BaseModel(id='123',
                              created_at=datetime.now(),
                              updated_at=datetime.now())
        self.assertEqual(new_model.id, '123')

    def test_init_method_without_arguments(self):
        new_model = BaseModel()
        self.assertIsInstance(new_model.id, str)
        self.assertIsInstance(new_model.created_at, datetime)
        self.assertIsInstance(new_model.updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
