import primez
import itertools


def boo(v):
    """returns the product combos of a prime distribution"""
    pv = list(v.keys())
    for c in itertools.product(*(range(x + 1) for x in v.values())):
        ret = 1
        for i in range(len(pv)):
            ret *= pv[i] ** c[i]
        yield ret


def bar(x, v, n):
    #    print("bar", x, v, n)
    if x < n:
        ret = 1
        for i, j in v.items():
            ret *= j // 2 + 1
        return ret
    else:
        c0 = 1
        bmax = 1
        for i, j in list(v.items()):
            if j % 2 == 1:
                c0 *= i
            if j // 2:
                v[i] = j // 2
                bmax *= i ** v[i]
            else:
                del v[i]

        ret = 0
        for b in boo(v):
            assert bmax % b == 0, "%s %s %s" % (v, bmax, b)
            if b + c0 * (bmax // b) ** 2 <= n:
                ret += 1
        return ret


"""finds b*b*c=x combos such as b+c < n"""


def foo(n):
    ret = 0
    for i in range(2, n - 1, 3):
        if i % 10000 == 0:
            print(i)

        k = i // 3

        v1 = primez.decompose(8 * k + 5)
        v2 = primez.decompose(k + 1)
        for key, val in v2.items():
            v1[key] = v1.get(key, 0) + val * 2

        b = bar((8 * k + 5) * (k + 1) ** 2, v1, n - i)

        ret += b
    return ret


def brute(n):
    for a in range(1, n - 1):
        ka = 8 * a ** 3 + 15 * a ** 2 + 6 * a - 1
        if ka % 27 != 0:
            continue
        ka //= 27

        for b in range(1, n - a):
            if ka % b**2 != 0:
                continue
            for c in range(1, n - a - b + 1):
                if b ** 2 * c == ka:
                    yield a, b, c
