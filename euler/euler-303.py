from itertools import product as prod

# shamelessly copied from problem 714, restricting the digitz as instructed


def gen_three(first, n):
    """gens n-digit numbers with digitz 0-2 starting with first"""
    base = first * 10 ** (n - 1)
    for p in prod(*((0, 1, 2),) * (n - 1)):
        ret = 0
        for x in p:
            ret *= 10
            ret += x
        yield ret + base


def go(n, m=15):
    v = list(range(1, n + 1))
    s = 0
    lenv = len(v)
    for ndigitz in range(1, m):
        for first_digit in (1, 2):
            for j in gen_three(first_digit, ndigitz):
                q = 0
                for k in range(lenv):
                    if q < k:
                        v[q] = v[k]
                    if j % v[k] == 0:
                        s += j // v[k]
                    else:
                        q += 1
                lenv = q
                if not lenv:
                    print("success", s)
                    return s
            print(ndigitz, first_digit, lenv)

    print("fail", s, lenv)


go(10000, 1000)


def count(v):
    d = {}
    for x in v:
        d[x] = d.get(x, 0) + 1
    return {a: b for a, b in d.items() if b > 1}
