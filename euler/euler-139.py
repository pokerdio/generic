# project euler problem 139

from itertools import count, islice


#from fractions import gcd


def make_pythagoras_triples(maxperimeter):
    ret = {}

    for m in range(1, int(1 + math.sqrt(maxperimeter)), 2):
        if m % 100 == 1:
            print(m)
        for n in range(1, m, 2):
            if gcd(m, n) == 1:
                abc = tuple(sorted((m * n, (m * m + n * n) // 2, (m * m - n * n) // 2)))
                assert (abc not in ret)
                p = sum(abc)
                if p < maxperimeter:
                    ret[abc] = (maxperimeter - 1) // p
    return ret


def go(maxperimeter=10**8):
    k = 0
    trips = make_pythagoras_triples(maxperimeter)
    for abc in trips:
        a, b, c = abc
        if c % (b - a) == 0:
            k += trips[abc]
    return k
