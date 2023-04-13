#!/usr/bin/python3

"""
a function for writing an object to txt file using a JSON rep
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
