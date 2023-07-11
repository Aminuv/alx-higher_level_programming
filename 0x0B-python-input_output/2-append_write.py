#!/usr/bin/python3

""" function append the end of the text."""


def append_write(filename="", text=""):
    """appending characters"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
