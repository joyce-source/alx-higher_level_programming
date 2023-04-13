#!/usr/bin/python3

"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""

import sys
from os import path
from typing import List
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


def add_item(filename: str, args: List[str]):
    """
    Function that adds all args to a Python list,then saves them to a file.
    """
    if path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    for arg in args:
        my_list.append(arg)

    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    filename = "add_item.json"
    args = sys.argv[1:]
    add_item(filename, args)
