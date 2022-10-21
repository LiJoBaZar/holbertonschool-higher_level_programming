#!/usr/bin/python3
"""Creating module"""
import json
import csv


class Base:
    """Define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        with open(filename, "w") as f:
            lst_j = list(map(lambda obj: obj.to_dictionary(), list_objs))
            f.write(cls.to_json_string(lst_j))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        dummy_instance = cls(**dictionary)
        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as f:
                list_obj_dict = cls.from_json_string(f.read())
                return list(map(lambda obj: cls.create(**obj), list_obj_dict))
        except:
            return []
