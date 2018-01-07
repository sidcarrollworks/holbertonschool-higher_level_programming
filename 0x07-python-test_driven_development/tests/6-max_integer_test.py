#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    test class
    """

    def test_int(self):
        """
        test max int
        """
        self.assertEqual(max_integer([1, 0, 4, 2, 10, -18]), 10)

    def test_none(self):
        """
        test empty value
        """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_empty(self):
        """
        test empty value
        """
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        """
        test negatives
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

if __name__ == '__main__':
    unittest.main()
