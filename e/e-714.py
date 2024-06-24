from itertools import product as prod


def gen_two(n):
    """gens base two numbers of n digits, tuple format, other than (1,1,1,...) """
    for p in prod(*((0, 1),) * (n - 1)):
        yield (1,) + p


def gen_duo(n, first):
    oneone = 0
    for _ in range(n):
        oneone = oneone*10 + 1

    for p in gen_two(n):
        a = 0
        for d in p:
            a *= 10
            if d:
                a += 1
        for j in range(10):
            yield a * first + (oneone-a) * j


def go(n, m=10):
    v = list(range(1, n + 1))
    s = 0
    lenv = len(v)
    for ndigitz in range(1, m):
        for first_digit in range(1, 10):
            lst = list(gen_duo(ndigitz, first_digit))
            lst.sort()
            for j in lst:
                q = 0
                for k in range(lenv):
                    if q < k:
                        v[q] = v[k]
                    if j % v[k] == 0:
                        s += j
                    else:
                        q += 1
                lenv = q
                if not lenv:
                    print("success", s)
                    return s
            print(ndigitz, first_digit, lenv)

    return s, v


go(50000, 1000)


def count(v):
    d = {}
    for x in v:
        d[x] = d.get(x, 0) + 1
    return {a: b for a, b in d.items() if b > 1}
