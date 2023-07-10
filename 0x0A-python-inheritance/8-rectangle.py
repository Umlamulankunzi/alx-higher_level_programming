#!/usr/bin/python3


"""Defines a class Rectangle

classes: 
	BaseGeometry: imported from module "7-base_geomtry"
	Rectangle: defined in module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """initialises new instances of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
