#!/usr/bin/env python3

# https://projecteuler.net/problem=27
#


from itertools import permutations


def p(n):
    return n * (3 * n - 1) // 2


v = [p(1)]
vset = set((v[0],))
n = 1

bestdif = None
besti, bestj = None, None

while True:
    n = n + 1
    if len(v) < n:
        pn = p(n)
        v.append(pn)
        vset.add(pn)

    if bestdif:
        if n % 1000 == 0:
            print("stupid check", bestdif, v[-1] - v[-2])

        if bestdif < v[-1] - v[-2]:
            print(besti, bestj, v[besti - 1], v[bestj - 1], bestdif)
            break

    for i in range(n - 2, -1, -1):
        psum = v[i] + v[n - 1]
        while psum > v[-1]:
            #            print("bomb", v, psum)
            v.append(p(len(v) + 1))
            vset.add(v[-1])
        if psum in vset:
            #            print("boom %d + %d == %d" % (v[i], v[n - 1], psum))

            pdif = v[n - 1] - v[i]
            if pdif in vset:
                print("hallelujah", n, i + 1, pdif)
                if not bestdif or pdif < bestdif:
                    bestdif = pdif
                    besti, bestj = i + 1, n
                    print("prelim", besti, bestj, bestdif)
