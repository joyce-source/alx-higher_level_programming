#!/usr/bin/python3

"""
This module contains a function for deserializing a JSON string into a Python object.

The `json` module is used for deserialization, so the function assumes that the input
string is a valid JSON representation of a Python object.

Example Usage:
--------------
json_string = '{"key": "value", "num": 42}'
my_dict = from_json_string(json_string)

# Output:
# {'key': 'value', 'num': 42}
"""


import json

def from_json_string(my_str):
    """
    Deserialize a JSON string into a Python object.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The Python object represented by the input JSON string.
    """
    return json.loads(my_str)
