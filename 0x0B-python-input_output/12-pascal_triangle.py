#!/usr/bin/python3

""" function return a list of list of intigers."""


def pascal_triangle(n):
    """the list of integeres"""

    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trin = triangle[-1]
        temp = [1]
        for i in range(len(trin) - 1):
            temp.append(trin[i] + trin[i + 1])
        temp.append(1)
        triangle.append(temp)
    return triangle
