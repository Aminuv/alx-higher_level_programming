#!/usr/bin/python3

""" function read the files."""


def read_file(filename=""):
    """ print the contents """

    with open(filname, encoding="utf-8") as f:
        print(f.read(), end="")
