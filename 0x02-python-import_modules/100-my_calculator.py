#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    _open = sys.argv[2]
    if _open != '+' and _open != '-' and _open != '*' and _open != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
        
    if _open == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif _open == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif _open == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
