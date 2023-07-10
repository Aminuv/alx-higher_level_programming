#!/usr/bin/python3

""" function that adds a new attribute"""


def add_attribute(*args):
    """dds a new attribute"""

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
