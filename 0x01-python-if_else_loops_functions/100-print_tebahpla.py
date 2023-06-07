#!/usr/bin/python3
for num in range(122, 96, -1):
    if num % 2 == 0:
        a = num
    else:
        a = num - 32
    print("{}".format(chr(a)), end="")
