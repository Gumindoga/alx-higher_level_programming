#!/usr/bin/python3
"""
This is a module that provides a function to look up the attributes
and methods of an object.
"""


def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object.
    """
    return dir(obj)
