#!/usr/bin/python3
"""
    Module that define a class Student
"""


class Student:
    """
        A class students that defines a student by:
        
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """Initialises Student instance.

        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """Gets dict representation of instance

            Args:
                attr (list): attribute names that are to be retrieved.
        """

        if attr is not None:
            dict_rep = {k: self.__dict__[k] for k in self.__dict__.keys() & attr}
            return dict_rep
        else:
            return self.__dict__
