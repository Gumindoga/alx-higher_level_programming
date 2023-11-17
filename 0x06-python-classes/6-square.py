#!/usr/bin/python3
"""
This module defines a Square class.

The Square class defines a square by a private instance attribute size.
The size of the square can be set at the time of creation and defaults to 0.
The size of the square can only be an integer and must be greater than or equal to 0.
The Square class also includes a method to calculate the area of the square.
The size attribute of the Square class can be accessed and modified through the size property.
The Square class also includes a method to print the square with the character #.
The position attribute of the Square class can be accessed and modified through the position property.
The position of the square is used when printing the square.
"""


class Square:
    """Defines a square.

    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square in 2D space

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new instance of the Square class.

        Args:
            size (int, optional): size of a side of the square. Defaults to 0.
            position (tuple, optional): position of the square in 2D space. Defaults to (0, 0).

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): position of the square in 2D space

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.

        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square.

        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #.

        If size is equal to 0, print an empty line.
        Position is used by using space.

        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))
