#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Defines a function that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices using NumPy
    Arguments:
    m_a: list of lists of integers or floats
    m_b: list of lists of integers or floats
    """

    # Multiply m_a and m_b using NumPy
	 
    product = np.matmul(m_a, m_b)
    
    return product
