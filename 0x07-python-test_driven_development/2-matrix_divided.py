#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.

The function takes two arguments: a matrix and a divisor.
The matrix must be a list of lists of integers or floats.
Each row of the matrix must be of the same size.
The divisor must be a number (integer or float) and can't be equal to 0.
The function returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix: The matrix to divide. Must be a list of lists of integers..
                Each row of the matrix must be of the same size.
        div: The number to divide the matrix by. Must be a number.
             Can't be equal to 0.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 dp.
    """
    lol_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"
    div_err = "div must be a number"
    zero_err = "division by zero"

    if not isinstance(matrix, list) or not all(
        (isinstance(row, list) for row in matrix)
    ):
        raise TypeError(lol_err)

    row_size = len(matrix[0])
    for row in matrix:
        if any(type(e) not in (int, float) for e in row):
            raise TypeError(lol_err)
        if len(row) != row_size:
            raise TypeError(row_err)

    if type(div) not in (int, float):
        raise TypeError(div_err)
    if div == 0:
        raise ZeroDivisionError(zero_err)

    return [[round(el / div, 2) for el in row] for row in matrix]
