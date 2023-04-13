#!/usr/bin/python3


class MyList(list):
    """
    A list subclass that provides a print_sorted method to print the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
