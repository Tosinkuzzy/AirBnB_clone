#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the BaseModel class."""
import models
from uuid import uuid4
=======
""" 
    Module for Base class
    Contains the Base class for the AirBnB clone console.
"""

import uuid
>>>>>>> c6fc2e3dc2f04a76b933f9f79b678cca765eeba1
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """Initialize a new BaseModel.

=======
        """
            Initialization of a Base instance.
>>>>>>> c6fc2e3dc2f04a76b933f9f79b678cca765eeba1
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
<<<<<<< HEAD
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
=======
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
            Returns a human-readable string representation
            of an instance.
        """

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
            Updates the updated_at attribute
            with the current datetime.
        """

        self.updated_at = datetime.now()
        storage.save()
>>>>>>> c6fc2e3dc2f04a76b933f9f79b678cca765eeba1

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
