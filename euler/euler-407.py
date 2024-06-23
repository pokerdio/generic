def M(n):
    ret = 0
    for i in range(1, n):
        if i * i % n == i:
            ret = i
    return ret


def MV(n):
    return [M(x) for x in range(1, n + 1)]


import primez


def compo_sum(d1, d2):
    ret = d1.copy()
    for i, j in d2.items():
        ret[i] = ret.get(i, 0) + j
    return ret


def my_decompose_iterate(aa):
    n = len(aa)
    aa = [i ** j for i, j in aa.items()]
    for i in range(2 ** n):
        m1, m2, k = 1, 1, 1
        for j in range(n):
            if i & k:
                m1 *= aa[j]
            else:
                m2 *= aa[j]
            yield m1, m2
            k *= 2


def go(n):
    a1 = {}  # decomposition of a -1
    ret = [1] * (n + 1)
    for i in range(2, n + 1):
        if i % 1000 == 1:
            print(i)
        a = primez.decompose(i)
        aa1 = compo_sum(a, a1)

        for j in primez.decompose_iterate(aa1):
            if j > i and j <= n:
                ret[j] = max(ret[j], i)

        a1 = a
    ret[1] = 0
    return ret[1:]
