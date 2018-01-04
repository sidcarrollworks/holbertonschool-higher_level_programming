#!/usr/bin/python3
"""
This module defines a square
"""


class Square:
    """A square that has stuff

    Attributes:
        size (int): The length of the side
    """
    def __init__(self, size=0):
        """Initialization of the square

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
