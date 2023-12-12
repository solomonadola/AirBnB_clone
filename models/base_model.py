#!/usr/bin/python3
"""
Thsi is a module that defines a base class for other classes.

This module contains the BaseModel class, which provides common attributes
and methods for other classes in the models package. The BaseModel class
implements the serialization and deserialization of instances to a JSON file.
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    A base class for other classes with common attributes and methods.

    Attributes:
        id (str): A unique identifier for each instance, assigned with uuid.
        created_at (datetime): The date and time of instance creation.
        updated_at (datetime): The date and time of the last instance update.

    Methods:
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance,
        with ISO-formatted strings for datetime attributes and
        a __class__ key with the class name.
    """

    def __init__(self):
        """
        initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Return a string representation of the BaseModel instance.

        Returns:
                str: A string containing the class name, id,
                and object's dictionary
        """
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of the object for serialization.

        Returns:
            dict: A dictionary containing all keys/values of the instance.
                  Includes '__class__', 'created_at', and 'updated_at'.

        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
