from fractions import Fraction as Fr
from builtins import sum


import primez


def pee(n):
    return primez.isprime(n) and "P" or "N"


def go(n, txt="PPPPNNPPPNPPNPN", f23=Fr(2, 3), f13=Fr(1, 3)):
    v = {n: (pee(n) == txt[0] and f23 or f13)}
    for c in txt[1:]:
        v2 = {}
        for i, p in v.items():
            p2 = p / 2
            if i > 1 and i < 500:
                v2[i - 1] = v2.get(i - 1, 0) + p2
                v2[i + 1] = v2.get(i + 1, 0) + p2
            if i == 1:
                v2[2] = v2.get(2, 0) + p
            if i == 500:
                v2[499] = v2.get(499, 0) + p

        for i in v2.keys():
            v2[i] = v2[i] * (pee(i) == c and f23 or f13)

        v = v2
#    print(v)
    return sum(list(v.values()))


print(sum(go(x) for x in range(1, 501)) / 500)
