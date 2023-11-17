#!/usr/bin/python3
"""
This module defines a Square class.

The Square class defines a square by a private instance attribute size.
"""


class Square:
    """Defines a square.

    Attributes:
        __size (int): size of a side of the square

    """

    def __init__(self, size):
        """Initializes a new instance of the Square class.

        Args:
            size (int): size of a side of the square

        """
        self.__size = size
