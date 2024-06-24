#!/usr/bin/env python3

#

from math import gcd


def simplify(a, b):
    if a == 0 or b == 0:
        return 0, 1
    com = gcd(a, b)
    a //= com
    b //= com
    return a, b


def fraction_eq(a1, b1, a2, b2):
    a1, b1 = simplify(a1, b1)
    a2, b2 = simplify(a2, b2)

    return (a1, b1) == (a2, b2)


def strpop(s, char):
    x = s.find(char)
    assert (x >= 0)
    return s[:x] + s[x + 1:]


def curiouser(a, b):
    sa, sb = str(a), str(b)
    for c in sa:
        if c != "0" and c in sb:
            popa, popb = int(strpop(sa, c)), int(strpop(sb, c))
            if fraction_eq(a, b, popa, popb):
                print("how curious: %d/%d == %d/%d" % (a, b, popa, popb))
                return simplify(popa, popb)


proda, prodb = 1, 1

for i in range(10, 100):
    for j in range(10, i):
        frac = curiouser(j, i)
        if frac:
            proda *= frac[0]
            prodb *= frac[1]

proda, prodb = simplify(proda, prodb)

print("total simplified curious product %d/%d" % (proda, prodb))
