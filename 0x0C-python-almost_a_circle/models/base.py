#!/usr/bin/python3
# Create a folder named models with an empty file __init__.py inside
# This file makes the folder a Python package

class Base:
    # private class attribute __nb_objects = 0
    __nb_objects = 0
    
    # class constructor: def __init__(self, id=None)
    def __init__(self, id=None):
        # if id is not None, assign the public instance attribute id with this argument value
        # otherwise, increment __nb_objects and assign the new value to the public instance attribute id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
