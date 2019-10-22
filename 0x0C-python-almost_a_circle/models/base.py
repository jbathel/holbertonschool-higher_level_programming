#!/usr/bin/python3
import json


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize id attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            my_list = []
        else:
            my_list = []
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(cls.__name__ + '.json', mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Square':
            dummy = cls(1)
            dummy.update(**dictionary)
            return dummy
        else:
            dummy = cls(1, 2)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        empty = []

        try:
            f = open(cls.__name__ + '.json')
            f.close()
        except FileNotFoundError:
            return empty

        with open(cls.__name__ + '.json', mode='r', encoding='utf-8') as f:
            new_list = cls.from_json_string(f.read())
        for i in new_list:
            empty.append(cls.create(**i))
        return empty
