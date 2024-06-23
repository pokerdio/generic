#!/usr/bin/env python3

import math
n = 600851475143


def make_primes(n):
    proc = 0
    n = int(n)
    s = set(range(2, n))
    ret = []
    while(True):
        if (len(s) == 0):
            return ret
        p = min(s)
        ret.append(p)

        new_proc = p * 100 // n
        if new_proc > proc:
            proc = new_proc
            print("%d%%" % proc)

        s = s - set(range(p, n, p))


p = make_primes(150000)
assert(len(p) >= 10001)
print(p[10000])
