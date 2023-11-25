#!/usr/bin/python3
"""
Module 100-matrix_mul
Defines a function that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices
    Arguments:
    m_a: list of lists of integers or floats
    m_b: list of lists of integers or floats
    """
    # Check if m_a and m_b are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # Check if m_a and m_b are lists of lists
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")

    # Check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # Check if each element of m_a and m_b is an integer or a float
    for row in m_a:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not all(isinstance(i, (int, float)) for i in row):
            raise TypeError("m_b should contain only integers or floats")

    # Check if m_a and m_b are rectangles
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Check if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Multiply m_a and m_b
    return [[sum(a * b for a, b in zip(r, c)) for c in zip(*m_b)] for r in m_a]
