#!/usr/bin/python3

"""function for adding new attribute"""


def add_attribute(obj, attr_bute, value):
    """
    Raise a TypeError exception,
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_bute, value)
