#!/usr/bin/python3
"""defines a square class"""


class Square:
    """Represent a square..."""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """return value to the size function"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current area of square"""
        return self.__size * self.__size
