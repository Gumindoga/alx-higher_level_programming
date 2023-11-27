#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class that represents a square.
    """

    def __init__(self, size: int):
        """
        Constructor of the square class.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self) -> int:
        """
        Calculates the area of the rectangle.
        """
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
