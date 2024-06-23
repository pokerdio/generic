#!/usr/bin/env python3


def divs(n):
    ret = {1, n}
    for i in range(2, 1 + n // 2):
        if n % i == 0:
            ret.add(i)
    return ret


def divs_tri(n):
    if n % 2 == 0:
        d1, d2 = divs(n // 2), divs(n + 1)
    else:
        d1, d2 = divs(n), divs((n + 1) // 2)
    return {i * j for i in d1 for j in d2}


def divcount(n):
    k = 1
    for i in range(1, 1 + n // 2):
        if n % i == 0:
            k += 1
    return k


def trinum(n):
    return n * (n + 1) // 2


def first_trinum(ndiv, maxn=100):
    maxd = 0
    for i in range(maxn):
        if not i % 100:
            print ("trying %d - current max is %d" % (i, maxd))
        k = len(divs_tri(i))
        if k > ndiv:
            assert(divcount(trinum(i)) == k)
            return i
        maxd = max(k, maxd)


print (trinum(first_trinum(500, 500000)))
