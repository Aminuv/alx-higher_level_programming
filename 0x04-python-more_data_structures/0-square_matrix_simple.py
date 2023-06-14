#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for num in matrix:
        matrix.append(list(map(lambda x: x**2, num)))
    return matrix
