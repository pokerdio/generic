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


def just_do_it(n):
    primes = make_primes(n + 1)
    ret = 1
    for p in primes:
        multiplicity = 1
        for i in range(2, n + 1):
            k = 0
            while i % p == 0:
                i /= p
                k += 1
            if k > multiplicity:
                multiplicity = k
        print ("multiplicity(%d) == %d" % (p, multiplicity))

        ret *= (p ** multiplicity)
    return ret


print (just_do_it(20))
