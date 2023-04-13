#!/usr/bin/python3

"""
script adds all arg to Python list and saves them to file in JSON format.

Functions:
    save_to_json_file(my_obj, filename):
        Saves a Python object to a file in JSON format.
        Args:
            my_obj: The Python object to be saved to the file.
            filename: The name of the file to be saved.
        Returns:
            None.

    load_from_json_file(filename):
        Loads a Python object from a file in JSON format.
        Args:
            filename: The name of the file to load the object from.
        Returns:
            The Python object loaded from the file.
"""

import json
import sys

from typing import List


def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """
    Saves a Python object to a file in JSON format.

    Args:
        my_obj: The Python object to be saved to the file.
        filename: The name of the file to be saved.

    Returns:
        None.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename: str) -> List[str]:
    """
    Loads a Python object from a file in JSON format.

    Args:
        filename: The name of the file to load the object from.

    Returns:
        The Python object loaded from the file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)


if __name__ == '__main__':
    # Add all arguments to a Python list.
    arguments = sys.argv[1:]
    # Load the list from the file, if it exists.
    try:
        saved_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        saved_list = []
    # Add the new arguments to the list.
    saved_list += arguments
    # Save the updated list to the file.
    save_to_json_file(saved_list, 'add_item.json')
