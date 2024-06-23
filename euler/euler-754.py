from builtins import sum
from math import gcd
import primez


def foo2(x, n):
    return sum(gcd(x, i) == 1 for i in range(x + 1, n + 1))


def gauss(n, mod=1000000007):
    ret = 1
    for i in range(2, n):
        ret = ret * pow(i, foo2(i, n), mod)
        if mod:
            ret %= mod
    return ret


def testfoo(n):
    for i in range(1, n):
        print(i, foo(i, n), foo2(i, n))


def above(low, p):
    x = low % p
    return p - x if x else 0


def interval_divz(low, high):
    a = [None] * (high - low)
    ln = len(a)
    for p in primez.iterate_primez(sqrt(high) + 2):
        start = above(low, p)
        for i in range(start, ln, p):
            if not a[i]:
                a[i] = [p]
            else:
                a[i].append(p)
    return a


def gen_index(n, data={}):
    """gens subset indexes that make odd and even set sizes"""
    if n in data:
        return data[n]

    odd = []
    even = []
    for i in range(1, 2 ** n):
        v = []
        for j in range(n):
            if i & (2 ** j):
                v.append(j)
        if len(v) % 2:
            odd.append(v)
        else:
            even.append(v)

    data[n] = (odd, even)
    return data[n]


def gen_monodivz(lst):
    n = len(lst)
    odd, even = gen_index(n)

    for i in odd:
        ret = 1
        for k in i:
            ret *= lst[k]
        yield 1, ret

    for i in even:
        ret = 1
        for k in i:
            ret *= lst[k]
        yield -1, ret


def go_one(x, divz, n, mod=1000000007):
    if not divz:
        divz = [x]
    else:
        x2 = x
        for div in divz:
            while x2 % div == 0:
                x2 //= div
        if x2 > 1:
            divz.append(x2)

    ret = n - x
    for sign, div in gen_monodivz(divz):
        count = (n // div) - (x // div)
        ret -= (sign * count)
    return ret


def go(n, ints=3, mod=1000000007):
    ret = 1
    for intie in range(ints):
        low = intie * n // ints + 1
        high = (intie + 1) * n // ints + 1
        print("doing %d - %d" % (low, high))

        divz = interval_divz(low, high)
        w = len(divz)

        for i in range(w):
            val = low + i
            pw = go_one(val, divz[i], n)
            ret = (ret * pow(val, pw, mod)) % mod
    return ret


#print(go(10**8, 100))
