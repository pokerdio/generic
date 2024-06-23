#!/usr/bin/env python3

# https://projecteuler.net/problem=85

from itertools import count


def onedee(x):
    return (x + 1) * x // 2


def twodee(x, y):
    return onedee(x) * onedee(y)


def go(n):
    best_score = n
    best = (-1, -1)
    k = 0
    for x in count(1):
        for y in count(1):
            k = k + 1
            new = twodee(x, y)
            score = abs(new - n)
            if score < best_score:
                best = (x, y)
                best_score = score

            if new > n:
                break
        if onedee(x) > n:
            break

    print("attempts count: ", k)
    return best
