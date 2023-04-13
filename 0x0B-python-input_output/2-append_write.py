#!/usr/bin/python3

"""
This module provides a function for appending a string to the end of a text file and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. If the file does not exist, it will be created.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added
