#!/usr/bin/python3

"""
module contains a function for deserializing a JSON string to a Python object.

So function assumes that input string is valid representation of Python object

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
