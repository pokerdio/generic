#!/usr/bin/python3
import re
import sys

from collections import Counter

def foo(x):
    return x * x

def main():
    start_freq = Counter()
    transition_freq = Counter()

    f = open (sys.argv[1])
    s = " ".join(s.strip().lower() for s in f.readlines())
    if (s[-1] != " "):
        s = s + " "
    for a, b in zip(s, s[1:]):
        if (b == " "):
            continue
        if (a == " "):
            start_freq.update([b])
        else:
            transition_freq.update([a + b])
    

if __name__ == "__main__":
    main()
