#!/usr/bin/env python3



def timestwo(n, m, mod):
    """returns n * 2^m % mod"""
    two, i = 2, 1

    while i <= m:
        if i & m:
            n = (n * two) % mod

        two = (two * two) % mod
        i = i * 2
    return n


print(timestwo(28433, 7830457, 10000000000) + 1)
