#!/usr/bin/python3
"""
This module contains a function that adds two integers.

The function takes two arguments, both of which must be integers or floats.
If either argument is not an integer or float, a TypeError is raised.
If either argument is a float, it is cast to an integer before addition.
The function returns the sum of the two arguments.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: The first integer or float to add. If a is not an integer or float,
           a TypeError is raised.
        b: The second integer or float to add. If b is not an integer or float,
           a TypeError is raised. Defaults to 98.

    Returns:
        The sum of a and b, as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
