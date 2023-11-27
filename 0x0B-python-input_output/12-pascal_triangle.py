#!/usr/bin/python3
"""
This module contains a function that generates Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        list of list of int: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle
