#!/usr/bin/python3
"""
This module defines a Square class.

The Square class defines a square by a private instance attribute size.
The size of the square can be set at the time of creation and defaults to 0.
The size of the square can only be an integer and must be greater than or equal to 0.
The Square class also includes a method to calculate the area of the square.
The size attribute of the Square class can be accessed and modified through the size property.
"""


class Square:
    """Defines a square.

    Attributes:
        __size (int): size of a side of the square

    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int, optional): size of a side of the square. Defaults to 0.

        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): size of a side of the square

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2
