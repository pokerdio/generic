import sys
from math import sqrt
from random import randint
input = sys.stdin.readline


def gen_input():
    while True:
        yield [int(c) for c in input().split()]


def gen_fake(n=100):
    yield [n, 3, 3]
    yield [randint(1, 10) for _ in range(n)]
    yield [1, 6]
    yield [5, 8]
    yield [2, 9]


def gen_fake():
    yield [6, 2, 3]
    yield [1, 2, 1, 1, 0, 3]
    yield [1, 6]
    yield [3, 5]


def gen_fake():
    yield [5, 3, 1]
    yield [1] * 5
    yield [1, 5]
    yield [2, 4]
    yield [1, 3]


def ints(g=gen_input()):
    return next(g)


def chopup(n):
    if n == 1:
        return [0, 1]
    chop_size = int(sqrt(n))
    return [0, *range(chop_size, n - 1, chop_size), n]


def go():
    n, m, k = ints()
    a = [0] + ints()
    n += 1
    for i in range(1, n):
        a[i] ^= a[i - 1]  # a[i] gets the prefix xor of first i items
    query = [ints() for _ in range(m)]
    for i, lr in enumerate(query):
        query[i] = (lr[0] - 1, lr[1])
    chops = chopup(n + 1)

    twotwenty = 2 ** 20
    v = [0] * twotwenty  # xoring of numbers up to 1m can result up to 2**20
    ret = {}

    for start, stop in zip(chops[:-1], chops[1:]):
        #print(f"STAGE {start}-{stop}")
        for i in range(twotwenty):
            v[i] = 0

        subquery = [lr for lr in query if lr[0] >= start and lr[0] < stop]
        subquery = sorted(subquery, key=lambda pair: pair[1])

        l = start
        r = start - 1
        count = 0

        for query_pair in subquery:
            newl, newr = query_pair
            #print(f"query {newl}-{newr}")
            # grow r
            for i in range(r + 1, newr+1):
                #print(f"r growing {i}")
                count += v[k ^ a[i]]
                v[a[i]] += 1
            if newl > l:  # chop l
                for i in range(l, newl):
                    #print(f"l chopping {i}")
                    if k == 0:
                        count -= (v[a[i]] - 1)
                    else:
                        count -= v[k ^ a[i]]
                    v[a[i]] -= 1
            elif newl < l:
                for i in range(l - 1, newl - 1, -1):
                    #print(f"l growing {i}")
                    count += v[k ^ a[i]]
                    v[a[i]] += 1
            r = newr
            l = newl
            ret[query_pair] = count
    for query_pair in query:
        print(ret[query_pair])


go()
