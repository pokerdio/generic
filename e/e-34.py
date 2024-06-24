#!/usr/bin/env python3

#

from math import gcd


def fact(n):
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k


def curious(n):
    s = 0
    for a in str(n):
        s += fact(int(a))
    return s == n


sum_curious = 0

for i in range(3, 2600000):
    if curious(i):
        print(i)
        sum_curious += i


print(sum_curious)
