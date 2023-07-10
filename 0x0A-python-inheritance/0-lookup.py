#!/usr/bin/python3

"""Module defining function that returns attributes and methids of an obj"""


def lookup(obj):
    """Function that returns the list of available attributes and methods,
    of an object

    Args:
        obj (any): instance obj of any class

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
