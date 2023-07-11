#!/usr/bin/python3

"""
Module defining function that reads a text file (UTF8) and
prints it to stdout:
"""


def read_file(filename=""):
    """Reads file (UTF8) and prints it to stdout

    Args:
        filename (str): name of the file
    """
    with open(filename, "r", encoding="UTF-8") as f:
            print(f.read(), end="")