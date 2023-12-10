#!/usr/bin/python3
"""
this module implements the serialization and deserialization of
BaseModel instances. This module defines a function that
converts a BaseModel instance to a JSON string and saves it
to a file. It also defines a function that reads a JSON string
from a file and creates a BaseModel instance from it. This way,
the BaseModel instances can be persisted and restored across
different executions of the program.
"""


class FileStorage:
    """This class represents an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the __objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the stored JSON file __file_path to __objects,
        if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
