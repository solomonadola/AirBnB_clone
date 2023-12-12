#!/usr/bin/python3
"""Module for FileStorage class.

This module defines the FileStorage class, responsible for
serializing instances to a JSON file
and deserializing a JSON file to instances.
It provides methods to manage a dictionary (__objects)
that stores instances with keys formatted as '<class name>.<id>'.

Attributes:
    __file_path (str): The path to the JSON file.
    __objects (dict): A dictionary to store instances by keys.

Methods:
    all(self): Returns the dictionary __objects.
    new(self, obj): Sets in __objects the obj with key <obj class name>.id.
    save(self): Serializes __objects to the JSON file (path: __file_path).
    reload(self): Deserializes the JSON file
    to __objects (only if the JSON file (__file_path) exists).
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a
    JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        fsto = FileStorage.__objects.items()
        obj_dict = {key: obj.to_dict() for key, obj in fsto}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists)."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
