#!/usr/bin/env python3

#


def go(n):
    k = 1
    s = 1
    for i in range(3, n + 1, 2):
        for _ in range(4):
            k += i - 1
            s += k

    return s
