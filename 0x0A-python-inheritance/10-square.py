#!/usr/bin/python3
"""
This module contains a class Square that inherits from Rectangle.
"""


class BaseGeometry:
    """
    Base class for geometrical objects.
    """

    def area(self):
        """
        Calculates the area of the object. Not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.
    """

    def __init__(self, width, height):
        """
        Constructor of the rectangle class.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


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
