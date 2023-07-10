#!/usr/bin/python3

"""checks for only subclass"""


def inherits_from(obj, a_class):
    """Determines if obj is an instance of a class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
