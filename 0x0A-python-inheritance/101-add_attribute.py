#!/usr/bin/python3

""" function that adds a new attribute"""


def add_attribute(*args):
    """
    dds a new attribute
    """

    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")
