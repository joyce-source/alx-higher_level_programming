#!/usr/bin/python3

def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, string and boolean) for JSON serialization of an object.

    Args:
        obj: an instance of a Class.

    Returns:
        A dictionary containing the attributes of the given object.

    """
    return obj.__dict__
