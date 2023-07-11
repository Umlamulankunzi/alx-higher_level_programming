#!/usr/bin/python3
"""
Module defining function that writes a string to a text file.
Using UTF-8 encoding and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes text to file and returns number of chars written

    Args:
        filename (str): name of the file
        text (str): text to be written

    Returns:
        int: number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
