#!/usr/bin/python3



"""
Defines a class Square

classes: 
	Rectangle: imported from module "9-rectangle"
	Square defined in module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialises new instance of class Square.

        Args:
            size (int): size of side of square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the Square.

        Returns:
            str: representation of square.
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculates area of square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
