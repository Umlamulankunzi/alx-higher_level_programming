#!/usr/bin/python3

"""
This module provides a class blueprint for a Square object.
"""


class Square:
    """class implementing square object
    """

    def __init__(self, size=0):
        """init function sets up the instance attributes

        Args:
            size (int): size of square object side. Defaults to 0.

        Raises:
            TypeError: if value is not of type int or float
            ValueError: if value is < 0
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """property method to get private instance attribute

        Returns:
            int: size of square side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value for private instance attribute

        Args:
            value (int): new value to set as size value

        Raises:
            TypeError: if value is not of type int or float
            ValueError: if value is < 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """calculates area of square class

        Returns:
            int: area of class
        """
        return self.size ** 2

    def __eq__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() == other.area()

    def __gt__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() < other.area()

    def __ne__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() != other.area()

    def __le__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """comparison of instances of Square class

        Args:
            other (Square): _description_

        Returns:
            bool: true or false
        """
        return self.area() >= other.area()
