#!/usr/bin/env python3


max_pali = 0


def pali(x):
    x = str(x)
    return x == "".join(reversed(x))


for i in range(100, 1000):
    for j in range(i + 1, 1000):
        p = i * j
        if (pali(p)) and p > max_pali:
            max_pali = p

if max_pali > 0:
    print ("Success: %d" % max_pali)
else:
    print ("FAILURE")
