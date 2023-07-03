#!/usr/bin/python3

"""
Module defines a Rectangle Class
"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """instance initialisation method

        Args:
            width (int, optional): value of rectangle width. Defaults to 0.
            height (int, optional): value of rectangle height. Defaults to 0.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method to access private attribute self.__width

        Returns:
            int: value of private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter of private instance attribute self.__width

        Args:
            value (int): new value to set private attribute with

        Raises:
            TypeError: if value is not int
            ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method to access private attribute self.__height

        Returns:
            int: value of private attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter of private instance attribute self.__height

        Args:
            value (int): new value to set private attribute with

        Raises:
            TypeError: if value is not int
            ValueError: if value less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
