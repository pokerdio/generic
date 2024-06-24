#!/usr/bin/env python3

# https://projecteuler.net/problem=61
#


def go(n=1000, count=3):
    d = {}

    for i in range(n):
        cube = i ** 3
        s = str(sorted(str(cube)))
        if s in d:
            d[s].append(cube)
            if len(d[s]) == count:
                print(d[s])
                return
        else:
            d[s] = [cube]
