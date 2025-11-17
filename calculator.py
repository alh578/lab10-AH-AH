# https://github.com/alh578/lab10-AH-LD
# Partner 1: Adam Hoshimov
# Partner 2: Luke Dutrow

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("division by zero")
    else:
        return b / a

def logarithm(a, b):
    if b <= 0 or a <= 0:
        raise ValueError
    else:
        return math.log(b, a)

def exp(a, b):
    return a ** b
