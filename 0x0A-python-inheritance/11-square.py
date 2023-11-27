#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class that represents a square.
    """

    def __init__(self, size):
        """
        Constructor of the square class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
