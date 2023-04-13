#!/usr/bin/python3

"""
function appends a string to end of txt file and returns number of char added
"""


def append_write(filename="", text=""):
    """
    Adds a string to the end of a txt file and returns the length of the string

    Args:
        filename (str): name of file to append will be created if doesnt exist
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        num_chars_added = file.write(text)
        return num_chars_added
