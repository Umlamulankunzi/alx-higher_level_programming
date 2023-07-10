#!/usr/bin/python3


"""
Defines a class MyInt that inherits from int.
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """Defines a class MyInt that inherite from int.

    Args:
        int (int): value
    """
    def __init__(self, value):
        """initialises new instance of class MyInt.

        Args:
            value (int): integer.
        """
        self.__value = value

    def __eq__(self, other):
        """ equal magic method

        Args:
            other (int): integer.

        Returns:
            bool: True or False.
        """
        return self.__value != other

    def __ne__(self, other):
        """Not equal magic magic

        Args:
            other (int): integer.

        Returns:
            bool: True or False
        """
        return self.__value == other
