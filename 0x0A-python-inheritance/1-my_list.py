#!/usr/bin/python3
"""
Defines an inherited list class mylist
"""


class MyList(list):
    """
    A list subclass that print_sorted method to print list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
