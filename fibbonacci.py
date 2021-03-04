import pytest

def fibbonacci_f(x):
    if (x == 0):
        return 0
    elif(x == 1 or x == 2):
        return 1
    else:
        return fibbonacci_f(x-1) + fibbonacci_f(x-2)


def factorial_f(x):
    if (x == 1):
        return 1
    else:
        return x * factorial_f(x-1)

def test_fibbonacci_f():
    assert fibbonacci_f(4) == 5