#!/usr/bin/env python3

#


tri = set(x * (x + 1) // 2 for x in range(100))


def val(s):
    return sum(ord(x) - ord('A') + 1 for x in s.upper())


with open("p042_words.txt") as f:
    words = f.read().replace('"', "").split(",")
    print(sum(val(w) in tri for w in words))
