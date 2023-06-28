#!/usr/bin/python3
"""Defines the MagicClass matching exactly the bytecod Holberton."""


import math


class MagicClass:
    """represents a circle"""
    def __init__(self, radius=0):
        """Initializes a Magic Class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculaes the area of circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """Calculates the circumference of circle"""
        return 2 * math.pi * self.__radius
