#!/usr/bin/python3
"""
A module that defines a base class for other classes.

This module contains the BaseModel class, which provides common attributes
and methods for other classes in the models package. The BaseModel class
implements the serialization and deserialization of instances to a JSON file.
"""

import uuid
from datetime import datetime


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

    def __init__(self, *args, **kwargs):
        """
        initializes object using dictionary if given otherwise
        it gives default value
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """string repr of obj"""
        return '[{}] ({}) {}'.format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all key/value of __dict__
        of the instance"""
        dic = vars(self).copy()
        dic['__class__'] = self.__class__.__name__
        dic['updated_at'] = self.updated_at.isoformat()
        dic['created_at'] = self.created_at.isoformat()
        return dic
