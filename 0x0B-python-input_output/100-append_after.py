#!/usr/bin/python3

"""function insert a line of textto a files."""


def append_after(filename="", search_string="", new_string=""):
    """insert the text"""

    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, 'w') as w:
        w.write(text)
