#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Defines a class for testing the function max_integer
    """

    def test_max_integer(self):
        """
        Tests max_integer with a set of lists
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_max_integer_errors(self):
        """
        Tests max_integer for type errors and value errors
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "3", 4])
        with self.assertRaises(TypeError):
            max_integer(1, 2, 3, 4)
