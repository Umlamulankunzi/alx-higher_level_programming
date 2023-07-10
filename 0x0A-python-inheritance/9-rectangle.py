#!/usr/bin/python3


"""
Defines a class Rectangle

classes:
    BaseGeometry: imported from module "7-base_geomtry"
    Rectangle: defined in module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """initialises new instance of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area of Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return str representation of Rectangle.

        Returns:
            str: str representation of Rectangle.
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
