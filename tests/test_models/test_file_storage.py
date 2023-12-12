import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setting up TestFileStorage class...')

    @classmethod
    def tearDownClass(cls):
        print('Tearing down TestFileStorage class...')
        # Clean up by removing the test JSON file if it exists
        test_file_path = "test_file.json"
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

    def setUp(self):
        print('Setting up a test...')
        self.file_storage = FileStorage()
        self.base_model = BaseModel()
        self.file_path = "test_file.json"
        self.file_storage._FileStorage__file_path = self.file_path
        self.file_storage._FileStorage__objects = {}

    def tearDown(self):
        print('Tearing down a test...')

    def test_all_method(self):
        # Add an object to __objects before calling all()
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.file_storage._FileStorage__objects[key] = self.base_model

        all_objects = self.file_storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.file_storage.new(self.base_model)

    def test_save_method(self):
        self.file_storage.new(self.base_model)
        self.file_storage.save()

        # Check if the file has been created
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_method(self):
        # Save an object to a test file
        key = "{}.{}".format(self.base_model.__class__.__name__,
                             self.base_model.id)
        self.file_storage._FileStorage__objects[key] = self.base_model
        with open(self.file_path, 'w') as file:
            json.dump({key: self.base_model.to_dict()}, file)

        # Reload the data and check if it matches the saved object
        self.file_storage.reload()
        reloaded_objects = self.file_storage.all()
        self.assertIn(key, reloaded_objects)
        reloaded_model = reloaded_objects[key]
        self.assertEqual(reloaded_model.id, self.base_model.id)


if __name__ == '__main__':
    unittest.main()
