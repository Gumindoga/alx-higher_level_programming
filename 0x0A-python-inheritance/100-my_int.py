#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int.
"""


class MyInt(int):
    """
    A class that represents an integer with inverted comparison operators.
    """

    def __eq__(self, other):
        """
        Inverted equality comparison.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverted inequality comparison.
        """
        return super().__eq__(other)
	