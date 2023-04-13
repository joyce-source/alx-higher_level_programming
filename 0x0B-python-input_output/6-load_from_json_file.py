#!/usr/bin/python3

"""
This module provides functions to handle JSON data
"""


import json


def load_from_json_file(filename):

    """
        Load an object from a JSON file.

    Argsef load_from_json_file(filename)

    filename: A string representing the path to the JSON file.

    Returns:
        The Python object represented by the JSON filename
"""


with open(filename, "r") as f:
    obj = json.load(f)
    return obj
