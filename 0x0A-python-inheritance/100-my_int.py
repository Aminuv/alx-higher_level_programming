#!/usr/bin/python3

""" a class MyInt that inherits from int """


class MyInt(int):
    """ The Class """
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
