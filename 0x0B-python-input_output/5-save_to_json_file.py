#!/usr/bin/python3

"""function writes an object of text files."""
import json


def save_to_json_file(my_obj, filename):
    """writes the object"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
