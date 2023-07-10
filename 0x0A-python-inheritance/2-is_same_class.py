#!/usr/bin/python3


"""
Defines a function is_same_class Returns
True if the object is exactly an instance of the,specified class;
Otherwise False
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the,
    specified class ; otherwise False

    Args:
        obj (any): object.
        a_class (any): class.

    Returns:
        boolean: True or False
    """
    return type(obj) == a_class
