#!/usr/bin/python3
class Student:
    """
    Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): the student's first name.
        last_name (str): the student's last name.
        age (int): the student's age.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): a list of attribute names to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            A dictionary representing the student instance.
    """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
