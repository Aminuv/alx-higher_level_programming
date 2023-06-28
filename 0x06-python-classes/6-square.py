#!/usr/bin/python3
"""defines a square class"""


class Square:
    """Represent a square..."""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of square"""
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return

        for i in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print("", end="")
            for z in range(self.__size):
                print("#", end="")
            print("")
