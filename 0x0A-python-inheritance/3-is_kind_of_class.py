#!/usr/bin/python3


"""
Defines a function is_kind_of_class
That checks if the object is an instance of a class,
or parent ot the spefified class

"""


def is_kind_of_class(obj, a_class):
    """That checks if the object is an instance of or parent of class

    Args:
        obj (any): object to check type.
        a_class (any): type of type to check.

    Returns:
        bool: True or False.
    """
    return isinstance(obj, a_class)
