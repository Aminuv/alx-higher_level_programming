#!/usr/bin/python3

"""
   Defines a class-checking function
"""


def is_same_class(obj, a_class):
    """checks if obj is exactly an instance of given class"""
    if type(obj) != a_class:
        return False
    return True
