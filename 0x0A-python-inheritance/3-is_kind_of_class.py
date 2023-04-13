#!/usr/bin/python3
"""Define a class and inherited class-checking function"""


def is_kind_of_class(obj. a_class):
    """
    Check if an object is an instance or inherited instance of a class
    Arg
    obj(any): the object to Check
    a_class(type): the class to match the type of obj to
    Returns:
    if obj is an instance or inherited instance of a_class - True
    otherwise - False
    """
    if isinstance(ob, a_class):
        return True
    return False
