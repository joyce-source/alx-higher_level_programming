#!/usr/bin/python3

"""
This module provides a function for reading a text file and printing its contents to the standard output.
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
