#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    num = len(argv) - 1
    if num == 0:
        print("{} arguments.".format(num))
    elif num == 1:
        print("{} argument:".format(num))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(num))
        num = 1
        for arg in argv[1:]:
            print("{}: {}".format(num, arg))
            num += 1
