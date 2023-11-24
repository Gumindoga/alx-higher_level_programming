#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

The function takes two arguments: a matrix and a divisor.
The matrix must be a list of lists of integers or floats.
Each row of the matrix must be of the same size.
The divisor must be a number (integer or float) and can't be equal to 0.
All elements of the matrix are divided by the divisor, rounded to 2 decimal places.
The function returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: The matrix to divide. Must be a list of lists of integers or floats.
                Each row of the matrix must be of the same size.
        div: The number to divide the matrix by. Must be a number (integer or float).
             Can't be equal to 0.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in row] for row in matrix]
