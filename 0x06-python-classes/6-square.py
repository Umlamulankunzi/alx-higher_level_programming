#!/usr/bin/python3
class Square:
    """class implementing square object
    """

    def __init__(self, size=0, position=(0, 0)):
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

        if (isinstance(position, tuple) and len(position) == 2 and
                isinstance(position[0], int) and isinstance(position[1], int)
                and position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def position(self):
        """getter for self.__position

        Returns:
            tuple: tuple containing 2 integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for instance attribute self.__position

        Args:
            value (tuple): new value for instance attribute

        Raises:
            TypeError: if value not tuple of exactly 2 positive int values
        """
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int)
                and value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            for _ in range(self.position[1]):
                print()

            for _ in range(self.size):
                print(" " * self.position[0], end="")

                for _ in range(self.size):
                    print("#", end="")
                print()
