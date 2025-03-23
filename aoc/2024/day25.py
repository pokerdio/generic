import re
from itertools import product
from random import random

schem = [[s.strip() for s in sch.strip().split("\n")] for sch in open("day25_input.txt").read().split("\n\n")]
key = []
lock = []

def toHeights(sch):
    ret = [-1] * 5
    if sch[0] == ".....":
        sch = list(reversed(sch))

    for i in range(1, len(sch)):
        for j, c in enumerate(sch[i]): 
            if c == '.' and ret[j] == -1:
                ret[j] = i-1
    return ret

for sch in schem:
    if sch[0] == "#####":
        lock.append(toHeights(sch))
    else:
        key.append(toHeights(sch))


def problim():
    ret = 0
    for k in key:
        for l in lock:
            if max(k[i] + l[i] for i in range(5)) <= 5:
                ret += 1

    return ret

problim()
