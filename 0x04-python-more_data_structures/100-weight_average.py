#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    i = sum(list(map(lambda x: x[0] * x[1], my_list)))
    j = sum(list(map(lambda x: x[1], my_list)))
    result = i / j
    return result
