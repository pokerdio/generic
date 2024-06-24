
from itertools import count


def ispali(n):
    return n == int("".join(reversed(str(n))))


def go(n):
    for maxroot in count(1):
        if maxroot**2 + (maxroot + 1) ** 2 > n:
            break
    maxroot += 5
    print(maxroot)
    s = 0
    sqsum = []
    for i in range(maxroot):
        s += i ** 2
        sqsum.append(s)

    ret = []
    for i in range(maxroot - 1):
        for j in range(i + 2, maxroot):
            s = sqsum[j] - sqsum[i]
            if s < n and ispali(s):
                ret.append((s, i, j))

    return ret, sum(list(set([x[0] for x in ret])))
