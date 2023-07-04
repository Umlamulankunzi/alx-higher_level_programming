#!/usr/bin/python3

"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test Suite for max_integer function"""

    def test_max_integer_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_no_args_passed(self):
        self.assertIsNone(max_integer())

    def test_valid_list(self):
        self.assertEqual(max_integer([1, 2, 6, 7]), 7)

    def test_max_integer_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_integer_negative_numbers(self):
        self.assertEqual(max_integer([-5, -4, -3, -2, -1]), -1)

    def test_max_integer_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 0, 10, -5, 5]), 10)

    def test_max_integer_string(self):
        self.assertEqual(max_integer("hello"), "o")

    def test_max_integer_passing_non_iterable(self):
        with self.assertRaises(TypeError):
            max_integer(5)
