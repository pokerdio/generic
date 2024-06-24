#!/usr/bin/env python3

# https://projecteuler.net/problem=27
#


from itertools import permutations


def foo():
    primez = sorted([17, 13, 11, 7, 5, 3, 2])
    total = 0

    for x in permutations("1234567890"):
        s = "".join(x)
        if s[0] != '0':
            okay = True
            for i in range(6, -1, -1):
                if int(s[i + 1: i + 4]) % primez[i] != 0:
                    okay = False
                    break
            if okay:
                total += int(s)

    return total


print(foo())
