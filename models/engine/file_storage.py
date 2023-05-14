#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""File Storage Module
This module is in charge of the storage of the
classes and their management.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import path


class FileStorage:
    """File Storage Class
    This is the File Storage module.
    Attributes:
        __file_path (str): This is the path of the JSON file in which
            the contents of the `__objects` variable will be stored.
        __objects (dict): This store all the instances data
    """
    __file_path = 'objects.json'
    __objects = {}

    def all(self):
        """this fuction Gets the __objects info and Returns the content of the `__objects` class attribute.
        """
        return self.__objects

   
