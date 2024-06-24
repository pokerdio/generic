#!/usr/bin/env python3


def doit(n):
    return sum(range(1, n + 1)) ** 2 - sum([x ** 2 for x in range(1, n + 1)])


print(doit(100))
