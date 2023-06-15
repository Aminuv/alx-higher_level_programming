#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_string = roman_string.upper()

    _num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    out_num = 0
    old_num = 0

    for i in reversed(roman_string):
        new = _num[i]
        out_num += new if new >= old_num else -new
        old_num = new

    return out_num
