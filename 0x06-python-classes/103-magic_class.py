#!/usr/bin/python3

"""
This module provides a class blueprint for a MagicClass object.
"""


import math


class MagicClass:
    """MAgic class
    """
    def __init__(self, radius):
        """init method instantiates instance attributes

        Args:
            radius (int, float): radius

        Raises:
            TypeError: if radius not int or float
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculate area

        Returns:
            float or int: area
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """calculate circurmference

        Returns:
            float, int: circurmference
        """
        return 2 * math.pi * self.__radius
