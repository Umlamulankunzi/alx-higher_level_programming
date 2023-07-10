#!/usr/bin/python3


"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): parent list.
    """

    def print_sorted(self):
        """Prints a list in ascending order."""
        print(sorted(self))
