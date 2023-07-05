#!/usr/bin/python3
""" The divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given numbe"""
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        items_in_first_row = len(matrix[0])
        if len(row) != items_in_first_row:
            raise TypeError("Each row of the matrix must have the same size")
        for items in row:
            if not isinstance(items, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats')

    return [list(map(lambda item: round((item / div), 2), row)) for row in matrix]
