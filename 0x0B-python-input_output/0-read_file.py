#!/usr/bin/python3

"""
module provides a function for reading txt file and prints contents to stdout.
"""


def read_file(filename=""):
    """
    Reads the contents of a text file and prints them to the standard output.

    Args:
        filename (str): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
