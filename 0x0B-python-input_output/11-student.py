#!/usr/bin/python3
"""Module for Student class."""


class Student:
    '''Class for jsonification.'''

    def __init__(self, first_name, last_name, age):
        """Initialises instance of class

        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Geta dict attribute of obj

        Attributes:
            attrs (list): list of strings.
        """
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        """Loads attributes from json."""
        for key, value in json.items():
            self.__dict__[key] = value
