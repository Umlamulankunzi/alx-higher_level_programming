#!/usr/bin/python3
"""
Module defining function that creates an Object from a “JSON file”:
"""
import json


def load_from_json_file(filename):
    """Loads json obj from file

    Args:
        filename (str): name of the file

    Returns:
        (list, dict): python object
    """
    with open(filename, "r") as f:
        new_obj = json.load(f)
        return new_obj
