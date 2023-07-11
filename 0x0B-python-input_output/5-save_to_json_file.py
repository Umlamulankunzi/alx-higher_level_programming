#!/usr/bin/python3
"""
Module Defines a function that writes an Object to a text file
using a JSON formatted output
"""
import json


def save_to_json_file(my_obj, filename):
    """writes a python object to a text file in json format

    Args:
        my_obj (list, dict): python sobject
        filename (str): filenamr
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
