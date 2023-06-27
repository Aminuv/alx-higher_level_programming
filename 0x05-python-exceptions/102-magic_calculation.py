#!/usr/bin/python3
def magic_calculation(a, b):
    rest = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('too far')
            else:
                rest += (a ** b) / i
        except Exception:
            rest = a + b
            break
    return rest
