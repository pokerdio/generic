#!/usr/bin/env python3
# problem 10
import array


def make_primes2(n):
    """1000 times faster than the other one"""
    sieve = array.array("b", [0]) * n
    ones = array.array("b", [1]) * n

    ret = []
    for i in range(2, n):
        if sieve[i] == 0:
            ret.append(i)
            sieve[i: n: i] = ones[i: n: i]
    return ret


def make_primes(n, printit=False):
    proc = 0
    n = int(n)
    s = set(range(2, n))
    ret = []
    while(True):
        if (len(s) == 0):
            return ret
        p = min(s)
        ret.append(p)

        if printit:
            new_proc = p * 100 // n
            if new_proc > proc:
                proc = new_proc
                print("%d%%" % proc)

        s = s - set(range(p, n, p))


assert(make_primes(997) == make_primes2(997))


print(sum(make_primes2(2000000)))
