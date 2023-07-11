#!/usr/bin/python3

""" function create an Object from JSON."""
import json


def load_from_json_file(filename):
    """creat an object"""

    with open(filename) as f:
        return json.load(f)
