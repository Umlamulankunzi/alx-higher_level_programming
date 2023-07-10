#!/usr/bin/python3


"""
Defines a function inherits_from
that checks if the object is an instance of a class that inherited,
(directly or indirectly) from the specified class;
"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class inherited,
    (directly or indirectly) from the specified class ; Else False.

    Args:
        obj (any): object.
        a_class (any): type.

    Returns:
        bool: True or False..
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
