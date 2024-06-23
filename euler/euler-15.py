#!/usr/bin/env python3

# https:/projecteuler.net

data = {(0, 0): 1}


def go(m, n):
    mn = (m, n)
    if mn in data:
        return data[mn]
    ret = (0 if n == 0 else go(m, n - 1)) + (0 if m == 0 else go(m - 1, n))
    data[mn] = ret
    return ret
