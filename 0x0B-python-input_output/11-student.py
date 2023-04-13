#!/usr/bin/python3

"""This module contains the Student class."""


class Student:

    def __init__(self, first_name, last_name, age):
        """
    Initialize a new Student object.

    Args:
    first_name (str): The first name of the student.
    last_name (str): The last name of the student.
    age (int): The age of the student.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self, attrs=None):
        """
    Return the dictionary representation of a Student instance:

    Args (list, optional): List of attributes to retrieve. Defaults to None.
    Returns:
    dict: Dictionary representation of the Student instance.
    """

    if attrs is None:
        return self._dict_
    else:
        return {attr: getattr(self, attr) for attr if hasattr(self, attr)}

    def reload_from_json(self, json):
        """
    Replace all attributes of the Student instanceself.

    Args:
    json (dict): The dictionary containing the new attributes and their value.
    """
        for key, value in json.items():
            setattr(self, key, value)
