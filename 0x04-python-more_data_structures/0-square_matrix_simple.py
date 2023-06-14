#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix1 = []
    for num in matrix:
        matrix1.append(list(map(lambda x: x**2, num)))
    return matrix1
