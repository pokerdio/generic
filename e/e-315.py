#!/usr/bin/env python3

# https://projecteuler.net/problem=315
# clockz, ez

from bitarray import bitarray as ba


def init_primes(n):
    sieve = ba(n)
    sieve[:] = True
    primez = []
    for i in range(2, n):
        if sieve[i]:
            sieve[i * 2:n:i] = False
            primez.append(i)

    return primez


noms = {"0": "1111101",
        "1": "0101000",
        "2": "0110111",
        "3": "0101111",
        "4": "1101010",
        "5": "1001111",
        "6": "1011111",
        "7": "1101100",
        "8": "1111111",
        "9": "1101111"}


def digital_root(n):
    return sum((int(a) for a in str(n)))


def nom_to_str(nom):
    return "".join(noms[x] for x in str(nom))


def cost_trans(str1, str2):
    if len(str1) > len(str2):
        str2 = "0" * (len(str1) - len(str2)) + str2
    elif len(str2) > len(str1):
        str1 = "0" * (len(str2) - len(str1)) + str1
    return sum((1 if x != y else 0 for x, y in zip(str1, str2)))


def cost_max(n):
    ret = cost_trans("", nom_to_str(n))
    while True:
        n2 = digital_root(n)
        if n2 < n:
            ret += cost_trans(nom_to_str(n), nom_to_str(n2))
            n = n2
        else:
            break

    return ret + cost_trans(nom_to_str(n), "")


def cost_sam(n):
    ret = 0
    while True:
        ret += 2 * cost_trans("", nom_to_str(n))
        n2 = digital_root(n)
        if n2 < n:
            n = n2
        else:
            break
    return ret


def cost_delta_total(n1, n2):
    primez = [prime for prime in init_primes(n2 + 1) if prime >= n1]

    print("primez complete", len(primez))
    ret = 0

    for i in primez:
        ret += cost_sam(i)
        ret -= cost_max(i)
    return ret


print(cost_delta_total(10 ** 7, 2 * 10 ** 7))
