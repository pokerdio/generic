import primez
from builtins import sum


def go(n=10**6):
    pr = list(primez.iterate_primez(n))

    g = {}
    for p in pr:
        print(p)
        g[p] = []
        for p2 in pr:
            if p2 < p and p2 | p == p:
                g[p].append(p2)
    return g
