#!/usr/bin/python3
"""Calculaion the module"""



def matrix_divided(matrix, div):
    if not isinstance(matrix,list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div,(int,float)):
        raise TypeError("div must be a number")
    if div==0:
        raise ZeroDivisionError("division by zero")
    element_count=len(matrix[0])
    for m in matrix:
        if not isinstance(m,list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(m) != element_count:
            raise TypeError("Each row of the matrix must have the same size")

    new_list=[]
    for element in matrix:
            new_list.append([round(e/div,2) for e in element])

    return new_list
