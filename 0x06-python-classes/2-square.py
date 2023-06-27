#!/usr/bin/python3
class Square:
    """class implementing square object
    """

    def __init__(self, size=0):
        """init function sets up the instance attributes

        Args:
            size (int): size of square object side
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
