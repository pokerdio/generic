#!/usr/bin/env python3

# https://projecteuler.net/problem=61
#


import itertools


def go(n=5):
    k = 0
    for i in itertools.count(1):
        s = str(i ** n)
        if len(s) > n:
            return k
        if len(s) == n:
            print("%d**%d==%s" % (i, n, s))
            k += 1


print(sum([go(x) for x in range(1, 100)]))
