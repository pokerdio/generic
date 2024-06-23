import numpy as np


def go(n=64000000):
    v = np.zeros(n, np.int64)
    l = 0
    for i in range(1, n):
        if int(log(i) * 10) > l:
            l = int(log(i) * 10)
            print("%d/%d" % (l, log(n) * 10 + 1))
        v[i::i] += i * i

    s = 0
    print("summing up")
    for x in range(1, n):
        if int(sqrt(v[x])) ** 2 == v[x]:
            s += x
    return s
