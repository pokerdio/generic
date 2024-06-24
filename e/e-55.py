#!/usr/bin/env python3

# reversed version of itself, check if its a palindrome, etc.


def f(n):
    return n + int(str(n)[::-1])


def pali(n):
    return n == int(str(n)[::-1])


def islychrel(n):
    for i in range(50):
        n = f(n)
        if pali(n):
            return False
    return True


def go():
    return sum(islychrel(i) for i in range(2, 10000))
