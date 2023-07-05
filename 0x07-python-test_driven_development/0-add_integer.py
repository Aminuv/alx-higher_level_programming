#!/usr/bin/python3

"""modulle add intigers its add tow intigers"""



def add_integer(a, b=98):
    """the add integer"""
    if not isinstance(a,(int,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b,(int,float)):
        raise TypeError("b must be an integer")
    return (int(a)+int(b))
