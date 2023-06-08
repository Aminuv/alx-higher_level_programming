#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = len(argv) - 1

    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} arguments:".format(i))
    else:
        print("{} arguments:".format(i))

        for j in argv[1:]:
            print("{}: {}".format(i, j))
            i += 1
