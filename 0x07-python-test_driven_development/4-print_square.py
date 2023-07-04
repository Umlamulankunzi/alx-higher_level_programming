#!/usr/bin/python3

"""
Module that prints a square using '#' character
"""


def print_square(size):
    """prints a square with side equal @size using '#' character

    Args:
        size (int): size of square to print

    Raises:
        TypeError: if size is not int
        ValueError: if size less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
