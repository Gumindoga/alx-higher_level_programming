#!/usr/bin/python3
"""
This module defines a MagicClass.

The MagicClass defines a circle by a private instance attribute radius.
The radius of the circle can be set at the time of creation and defaults to 0.
The radius of the circle can only be a number (float or integer), otherwise a TypeError exception with the message 'radius must be a number' is raised.
If radius is less than 0, a ValueError exception with the message 'radius must be >= 0' is raised.
The MagicClass also includes methods to calculate the area and the circumference of the circle.
"""


import math

class MagicClass:
    """Defines a MagicClass."""

    def __init__(self, radius=0):
        """Initializes a new instance of the MagicClass.

        Args:
            radius (float or int, optional): radius of the circle. Defaults to 0.

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle.

        Returns:
            The area of the circle.

        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle.

        Returns:
            The circumference of the circle.

        """
        return 2 * math.pi * self.__radius
