#!/usr/bin/python3

"""
This module contains a function for serializing Python objects to JSON.

The `json` module is used for serialization, so the function assumes that the
input object can be serialized as JSON.

Example Usage:
--------------
my_dict = {"key": "value", "num": 42}
json_string = to_json_string(my_dict)

# Output:
# '{"key": "value", "num": 42}'
"""


import json

def to_json_string(my_obj):
    """
    Serialize a Python object to JSON format.

    Args:
        my_obj: The object to be serialized.

    Returns:
        str: The JSON representation of the input object as a string.
    """
    return json.dumps(my_obj)
