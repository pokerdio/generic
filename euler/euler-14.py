#!/usr/bin/env python3
# problem 14

import array

cache_N = 10**8
cache = array.array("L", [0]) * cache_N
cache[1] = 1


def cache_get(n):
    if n < cache_N and cache[n]:
        return cache[n]
    return 0


def cache_set(n, v):
    if n < cache_N:
        cache[n] = v


def go(n):
    r = cache_get(n)
#    print (n, r)
    if r:
        return r

    if n % 2:
        r = go(n * 3 + 1) + 1
    else:
        r = go(n // 2) + 1

    cache_set(n, r)
    return r


def do(n):
    max_go = 0
    max_i = 0

    for i in range(1, n):
        k = go(i)
        if k > max_go:
            max_go, max_i = (k, i)
    return max_i, max_go
