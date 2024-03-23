#!/usr/bin/env python3
""" A stroage module """
from os import path
import json

class FileStorage:
    """Represents a file storage"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """Return all objects"""
        return FileStorage.__objects

    def new(self, obj):
        """ Create new object """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serialize object to file"""

        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as file:
            obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
            json.dump(obj_dict, file)

    def reload(self):
        """ Deserialize object from file """

        if path.exists(FileStorage.__file_path):
                with open(FileStorage.__file_path, mode='r', encoding='utf-8') as file:
                    obj_dict = json.load(file)
