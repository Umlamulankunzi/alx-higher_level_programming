#!/usr/bin/python3
"""
Module defines a function that returns an object
(Python data structure) represented by a JSON string:
"""
import json


def from_json_string(my_str):
    """Converts json str to python object

    Args:
        my_str (str): json string
    Returns:
        any: object
    """
    return json.loads(my_str)
