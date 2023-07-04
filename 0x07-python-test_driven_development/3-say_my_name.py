#!/usr/bin/python3

"""
Module defines function to print name and last name
"""


def say_my_name(first_name, last_name=""):
    """prints first and last name

    Args:
        first_name (str): string first name
        last_name (str, optional): string last name. Defaults to "".

    Raises:
        TypeError: if first_name or last_name not of type str_
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
