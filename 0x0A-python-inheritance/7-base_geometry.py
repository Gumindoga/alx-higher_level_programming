#!/usr/bin/python3
"""
This module contains a class BaseGeometry with two public instance methods.
"""


class BaseGeometry:
    """
    A class that includes methods to calculate the area
    and validate integer values.
    """

    def area(self):
        """
        A method that raises an Exception with the message
        "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates that 'value' is a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
