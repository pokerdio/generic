#!/usr/bin/env python3
# problem 14

import array


cache = {1: 1}


def go(n):
    r = cache.get(n)
    if r:
        return r

    if n % 2:
        r = go(n * 3 + 1) + 1
    else:
        r = go(n // 2) + 1

    cache[n] = r
    return r


def do(n):
    max_go = 0
    max_i = 0

    for i in range(1, n):
        k = go(i)
        if k > max_go:
            max_go, max_i = (k, i)
    return max_i, max_go
