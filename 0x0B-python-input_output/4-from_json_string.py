#!/usr/bin/python3

""" function return an object of python."""
import json


def from_json_string(my_str):
    """return the object"""

    return json.loads(my_str)
