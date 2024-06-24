#!/usr/bin/env python3



from bitarray import bitarray as ba


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n + 1:i] = False
            primez.append(i)

    return primez


import itertools


def pats(n):
    if type(n) == int:
        n = str(n)

    for i in set(n):
        lst = [x for x in range(len(n)) if n[x] == i]

        for masked_digits in range(1, len(lst) + 1):
            for lst_subset in itertools.combinations(lst, masked_digits):
                pat = ("*" if x in lst_subset else n[x] for x in range(len(n)))
                yield "".join(pat)


def go(ndigits):
    low = 10 ** (ndigits - 1)
    high = 10 ** ndigits
    primes = [x for x in init_primes(high) if x >= low]
    data = {}
    for prime in primes:
        for pat in pats(prime):
            if pat not in data:
                data[pat] = []
            data[pat].append(prime)

    for pat, noms in data.items():
        if len(noms) == 8:
            high = min(high, min(noms))

    if high % 10 != 0:
        return high


for i in range(1, 10):
    a = go(i)
    if a:
        print(a)
        break
