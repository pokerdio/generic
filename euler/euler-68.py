#!/usr/bin/env python3

# https://projecteuler.net/problem=483
# repeated permutations


# the solution doesnt' work for large numbers sadly
from itertools import permutations as perms
from itertools import combinations as combs

sols = []


def solstr(inner, outter):
    #    print(inner, outter)
    s = ""
    for i in range(5):
        s = s + str(outter[i]) + str(inner[i]) + str(inner[(i + 1) % 5])
    return s


def solve_outter(outter):
    #    print("outter:", outter)
    inner = list(reversed(sorted(list(set(range(1, 11)) - set(outter)))))
    for p in perms(inner):
        #        print("perm:", p)
        a = outter[0] + p[0] + p[1]
        if (outter[1] + p[1] + p[2] == a) and (outter[2] + p[2] + p[3] == a) and \
           (outter[3] + p[3] + p[4] == a) and (outter[4] + p[4] + p[0] == a):
            sols.append(solstr(p, outter))


def solve_low(low):
    for c in combs(range(low + 1, 10), 3):
        # print(c)
        for p in perms(c + (10,)):
            solve_outter((low, ) + p)


def solve():
    for i in range(6, 0, -1):
        solve_low(i)


solve()

print(max(sols))
