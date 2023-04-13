#!/usr/bin/python3

"""
function writes string a txt file and returns the number of characters writen
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters written

    Args:
        filename (str): The name of the file to write to. Defaults to "".
        text (str): The string to write to the file. Defaults to "".

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        num_chars_written = file.write(text)
        return num_chars_written
