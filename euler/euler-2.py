#!/usr/bin/env python3


def fibo(maxn):
    assert(maxn > 2)
    i, j = 1, 2
    r = [1, 2]
    while True:
        i, j = j, i + j
        if j >= maxn:
            return r
        r.append(j)


print(sum([i for i in fibo(4000001) if i % 2 == 0]))
