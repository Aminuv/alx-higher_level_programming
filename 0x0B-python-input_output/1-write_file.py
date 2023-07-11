#!/usr/bin/python3

"""function writes a string."""


def write_file(filename="", text=""):
    """writes files"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
