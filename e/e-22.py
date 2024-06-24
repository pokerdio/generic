#!/usr/bin/env python3

# https://projecteuler.net/problem=22
# read csv names from p022_names.txt


with open("p022_names.txt") as f:
    s = f.read().replace('"', '')
    total = 0
    pos = 0
    for name in sorted(s.split(",")):
        score = 0
        for a in name:
            score += ord(a) - ord('A') + 1
        pos += 1
        total += score * pos

print(total)
