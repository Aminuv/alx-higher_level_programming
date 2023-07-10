#!/usr/bin/python3

""" raises an exception for class"""


class BaseGeometry:
    """raises exception with the message"""

    def area(self):
        raise Exception("area() is not implemented")
