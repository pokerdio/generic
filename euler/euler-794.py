from fractions import Fraction as F


def nums():
    ret = set()
    for i in range(2, 18):
        for j in range(0, i):
            ret.add(F(j, i))
    return sorted(ret)


def foo(n, s=nums()):
    ret = []

    idx = 0
    for f in [F(i/n) for i in range(1, n + 1)]:
        v = []
        while s[idx] < f:
            v.append(s[idx])
            idx += 1
            if idx >= len(s):
                break
        ret.append(v)
    return [set(l) for l in ret]
