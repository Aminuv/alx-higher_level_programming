#!/usr/bin/python3
"""
 THE List that inherit from list
"""


class MyList(list):
    """THE Inherits from list"""
    def print_sorted(self):
        """FOR PrintING the list but sorted """
        print(sorted(self))
