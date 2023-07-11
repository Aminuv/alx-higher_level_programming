#!/usr/bin/python3

""" function return a list of list of intigers."""


def pascal_triangle(n):
    """the list of integeres"""

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        trin = triangles[-1]
        temp = [1]
        for i in range(len(trin) - 1):
            temp.append(trin[1] + trin[i + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
