#!/usr/bin/env python3

#

from itertools import cycle


def read_comma_sep_nums(fname):
    with open(fname) as f:
        return [int(s) for s in f.read().split(",")]


def frequency(data, n):
    d = {}
    for i in range(len(data) + 1 - n):
        k = tuple(data[i:i + n])
        d[k] = d.get(k, 0) + 1
    return d


def decode(data, kode):
    return "".join(chr(x ^ y) for x, y in zip(data, cycle(kode)))


def go(n):
    data = read_comma_sep_nums("p059_cipher.txt")
    the = tuple(ord(c) for c in "the")

    d = frequency(data, 3)

    for i in sorted(set(d.values()), reverse=True):
        for key, val in d.items():
            if val == i:
                kode = tuple(x ^ y for x, y in zip(key, the))
                print("testing", kode)
                print(decode(data, kode))
                n -= 1
                if n < 0:
                    return


# after running go(3), we get the dekoding key is 103 111 100


print(sum(ord(c) for c in decode(read_comma_sep_nums("p059_cipher.txt"), (103, 111, 100))))
