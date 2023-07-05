#!/usr/bin/python3

"""Prints a text with 2 new lines"""


def text_indentation(text):
    """print a text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for ch in ".:?":
        text = (ch + "\n\n").join(
            [line.strip(" ") for line in text.split(ch)])

    print(f"{text}", end="")
