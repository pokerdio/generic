#!/usr/bin/env python3

#

max_entries = 100


def combine_prob_distrib(d1, d2):
    d = {}
    for n1, freq1 in d1.items():
        for n2, freq2 in d2.items():
            d[max(n1, n2)] = d.get(n, 0.0) + freq1 * freq2

    return d


def ev(d):
    return sum((x * y) for x, y in d.items())


def onebit():
    return {x: 0.5 ** x for x in range(1, max_entries)}


def go():
    d = onebit()
    for i in range(5):
        d = combine_prob_distrib(d, d)

    return ev(d)
