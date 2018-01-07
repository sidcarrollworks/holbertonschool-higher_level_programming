#!/usr/bin/python3
"""
    This module contains matrix divider
"""


def matrix_divided(matrix, div):
    """This function divides the matrix

    Args:
        matrix (matrix): the matrix to be divided
        div (int): number to divided matrix by

    Return:
        returns the quotient
    """

    typeMessage = 'matrix must be a matrix (list of lists) of integers/floats'

    if not isinstance(matrix, list):
        raise TypeError(typeMessage)

    if isinstance(matrix[0], list):
        length = len(matrix[0])

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    for row in matrix:

        if not isinstance(row, list):
            raise TypeError(typeMessage)

        if len(row) != length:
            raise TypeError('Each row of the matrix must have the same size')

        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(typeMessage)

    new_matrix = [[round(i / div, 2) for i in x] for x in matrix]

    return new_matrix
