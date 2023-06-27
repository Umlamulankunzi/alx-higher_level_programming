#!/usr/bin/python3
class Square:
    """class implementing square object
    """

    def __init__(self, size=0):
        """init function sets up the instance attributes

        Args:
            size (int): size of square object side. Defaults to 0.

        Raises:
            TypeError: if value is not of type int
            ValueError: if value is < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
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
            TypeError: if value is not of type int
            ValueError: if value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
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

    def my_print(self):
        """prints the square with character #
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("#", end="")
                print()
