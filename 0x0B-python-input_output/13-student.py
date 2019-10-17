#!/usr/bin/python3
class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

    def to_json(self, attrs=None):
        if attrs is not None:
            dict1 = {}
            for key in attrs:
                if key in self.__dict__:
                    dict1[key] = self.__dict__[key]
            return dict1
        return self.__dict__

    def reload_from_json(self, json):
        for key in self.__dict__:
            if key in json:
                self.__dict__[key] = json[key]
