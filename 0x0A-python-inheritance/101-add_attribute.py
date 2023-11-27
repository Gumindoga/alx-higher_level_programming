#!/usr/bin/python3
"""
This is a module that provides a function to add a new attribute to an object if it’s possible.
"""


def add_attribute(obj, name, value):
    """
    Function that adds a new attribute to an object if it’s possible.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
