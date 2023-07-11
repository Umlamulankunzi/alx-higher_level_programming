#!/usr/bin/python3
"""
Module that defines a function that returns
the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """Returns JSON representation of my_obj

    Args:
        my_obj (str): string to represent

    Returns:
        str: json representation
    """
    return json.dumps(my_obj)