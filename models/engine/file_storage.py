#!/usr/bin/python3
""" FileStorage Class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ class FileStorage that serializes instances to a
        JSON file and deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Public instance method that return the private
            attribute dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Public instance method that sets in __objects
            the obj with key <obj class name>.id.
        """
        set_v = {obj.__class__.__name__ + "." + obj.id: obj}
        FileStorage.__objects.update(set_v)

    def save(self):
        """ Public instance method that serializes __objects
            to the JSON file (path: __file_path).
        """
        with open(FileStorage.__file_path, mode="w") as _file:
            ob_dic = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            _file.write(json.dumps(ob_dic))

    def reload(self):
        """ Public instance method that deserializes the
            JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing.
            If the file doesnt exist, no exception should be raised).
        """
        try:
            with open(FileStorage.__file_path, mode="r") as _file:
                load = json.loads(_file.read())

                for k in load.keys():
                    name = load[k]["__class__"]
                    FileStorage.__objects[k] = eval(name)(**load[k])
        except:
            pass
