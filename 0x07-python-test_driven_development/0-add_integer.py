#!/usr/bin/python3


"""
Module defining an add function that adds two numbers together


"""


def add_integer(a, b=98):
    """adds two numbers together
    Returns: int
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
