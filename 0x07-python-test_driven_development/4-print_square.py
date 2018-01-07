#!/usr/bin/python3
"""
    Print a square
"""


def print_square(size):
    """THis function prints square

    Args:
        size (int): the size of the square
    """
    if size < 0 and isinstance(size, float):
        raise TypeError('size must be an integer')
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for col in range(size):
        for row in range(size):
            print('#', end='')
        print()
