#!/usr/bin/python3
"""
Module that defines a function that appends a string at the end of a
text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """Appends text at end of file and returns number of chars appended

    Args:
        filename (str): name of the file
        text (str): text to be written

    Returns:
        int: number of characters written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
