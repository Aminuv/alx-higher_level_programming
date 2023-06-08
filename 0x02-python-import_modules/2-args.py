#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = len(argv)

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments:".format(i))
    else:
        print("{} arguments:".format(i))

