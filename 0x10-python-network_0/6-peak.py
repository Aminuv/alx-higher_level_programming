#!/usr/bin/python3
""" A function that finds 'a peak' in a list of unsorted integers """

def find_peak(list_of_integers):
    """ a peak in the list """

    if list_of_integers is None or list_of_integers == []:
        return None
    else:
        return max(list_of_integers)
