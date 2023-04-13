#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    """
    # Get the object's dictionary of attributes and methods
    obj_dict = obj.__dict__

    # Get the object's list of attributes and methods
    obj_attributes = dir(obj)

    # Get the set of keys in the object's dictionary
    dict_keys = set(obj_dict.keys())

    # Get the set of attributes not in the object's dictionary
    non_dict_attributes = set(obj_attributes) - dict_keys

    # Return the list of attributes and methods
    return sorted(list(dict_keys) + list(non_dict_attributes))
