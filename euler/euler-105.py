from itertools import combinations


def subset_sums(s):
    ret = set((0,))  # 0 is the sum of the empty set
    for i in range(1, len(s) + 1):
        ret.update(sum(c) for c in combinations(s, i))
    return ret


def test(v):
    v = sorted(v)
    for i in range(1, (len(v) + 1) // 2):
        if sum(v[:i + 1]) <= sum(v[-i:]):
            return False  # smallest n items bigger than biggest n-1 items?
    return len(subset_sums(v)) == 2 ** len(v)
    # 2^n distinct sums from 2^n distinct subsets


def load():
    ret = []
    for s in open("p105_sets.txt").readlines():
        ret.append([int(w) for w in s.split(",")])
    return ret


def go():
    return sum(sum(s) for s in load() if test(s))
