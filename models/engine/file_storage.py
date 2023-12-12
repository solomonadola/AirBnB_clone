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
from models.user import User


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances.
    """
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    obj_class = globals().get(class_name)
                    if obj_class and issubclass(obj_class, BaseModel):
                        obj = obj_class(**value)
                        self.__objects[key] = obj
        except FileNotFoundError:
            pass
