#!/usr/bin/python3
"""
    This module is used to add things
"""


def add_integer(a, b):
    """Add integer function

    Args:
        a: an int
        b: an int

    Return:
        the sum of a and b
    """

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')

    return (a + b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
