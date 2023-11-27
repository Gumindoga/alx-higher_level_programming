#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    Returns:
        bool: True or False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
