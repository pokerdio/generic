from itertools import combinations
from math import factorial as f


def c(n, r):
    return f(n) // (f(r) * f(n - r))


def dominates(c1, c2):
    onetwo = True
    twoone = True
    for i, j in zip(sorted(c1), sorted(c2)):
        if i > j:
            onetwo = False
        if i < j:
            twoone = False
    return onetwo or twoone


def testk(n, k):
    """tests how many k subsets of a n-set need to be tested"""
    cs = list(set(c) for c in combinations(list(range(n)), k))
    count = 0
    for i in range(len(cs) - 1):
        c1 = cs[i]
        for j in range(i + 1, len(cs)):
            c2 = cs[j]
            if cs[i] & cs[j]:  # if there's a common subset, it suffices testing
                continue  # the pair of the uncommon elements from each subset
            if not dominates(c1, c2):
                count += 1
    return count


def test(n):
    return sum(testk(n, k) for k in range(1, n))
