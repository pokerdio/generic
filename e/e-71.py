#!/usr/bin/env python3

import itertools

from fractions import Fraction as Fr

of = Fr(3, 7)


def f(n):
    global of

    x = of * n

    if x == int(x):
        return (x - 1) / n
    else:
        return Fr(int(x), n)


x = max(f(i) for i in range(2, 1000001))
