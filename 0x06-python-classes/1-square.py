#!/usr/bin/python3

"""
This module provides a class blueprint for a Square object.
"""


class Square:
    """class implementing square object
    """
    def __init__(self, size):
        """init function sets up the instance attributes

        Args:
            size (int): size of square object side
        """
        self.__size = size
