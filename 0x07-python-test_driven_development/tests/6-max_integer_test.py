#!/usr/bin/python3
"""The Unittet for the max integer module"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """classe for test different."""

    def test_ordered(self):
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered(self):
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_beg(self):
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element(self):
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_float(self):
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_str(self):
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_str(self):
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_str(self):
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
