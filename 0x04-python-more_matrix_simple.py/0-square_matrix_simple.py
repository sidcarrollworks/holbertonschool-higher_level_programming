#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[i * i for i in x] for x in matrix]
    return new_matrix
