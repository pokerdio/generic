#!/usr/bin/env python3

# https://projecteuler.net/problem=38
#
import math


def go(p):
    n = p // 2 + 1
    d = [0] * (p + 1)
    for c in range(2, n):
        c2 = c * c
        for a in range(1, c):
            a2 = a * a
            b = int(math.sqrt(c2 - a2))
            if b > 0 and b * b + a2 == c2:
                print("%d^2 + %d^2 == %d^2" % (a, b, c))

                if a + b + c <= p:
                    d[a + b + c] += 1

    return max(range(p + 1), key=lambda x: d[x])
