#!/usr/bin/python3
"""Define the square for the class"""


class Square:
    """that square class"""

    def __init__(self, size=0):
        """initializes a size"""
        self.size = size

    @property
    def size(self):
        """returns the value of size to the call function"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size value"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """return the current area of the square."""
        return int(self.size) ** 2

    def __eq__(self, other):
        """Define the == comparision to the Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """compare the area of the square"""
        return self.area() != other.area()

    def __gt__(self, other):
        """compare another square with >"""
        return self.area() > other.area()

    def __ge__(self, other):
        """compare to another square with >="""
        return self.area() >= other.area()

    def __lt__(self, other):
        """compare to another square with <"""
        return self.area() < other.area()

    def __le__(self, other):
        """compare to another square with <="""
        return self.area() <= other.area()
