#!/usr/bin/python3
"""
This module contains a class MyList that inherits from list.

The MyList class has a method print_sorted
that prints the list in ascending order.
"""


class MyList(list):
    """
    A class that inherits from list.
    """

    def print_sorted(self):
        """
        A method that prints the list in ascending order.
        """
        print(sorted(self))
