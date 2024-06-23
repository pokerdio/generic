import numpy as np
import primez
from builtins import sum


def mobi(n):
    ret = np.ones(n + 1, dtype=np.int8)
    prod = np.ones(n + 1, dtype=np.int32)
    count = np.zeros(n + 1, dtype=np.uint8)
    for p in primez.iterate_primez(int(sqrt(n) + 2)):
        ret[p * p::p * p] = 0
        count[p * 2::p] += 1
        prod[p * 2::p] *= p

    for i in range(n + 1):
        if ret[i] and ((count[i] + (prod[i] < i)) % 2):
            ret[i] = -1
    return ret


def mertens(n):
    mby = mobi(n)
    ret = [0]
    s = 0
    for i in range(1, n + 1):
        s += int(mby[i])
        ret.append(s)
    return ret


def mertens_extra(n, buff, b2={}):
    if n < len(buff):
        return buff[n]
    if n in b2:
        return b2[n]

    s = 1
    n2 = int(sqrt(n))
    for i in range(1, n2 + 1):
        k = n // i - n // (i + 1)
        s -= buff[i] * k
        ni = n // i

        if ni != i and ni != n:
            if ni < len(buff):
                rec = buff[ni]
            elif ni in b2:
                rec = b2[ni]
            else:
                rec = mertens_extra(ni, buff, b2)
            s -= rec

    b2[n] = s
    return s


def mertens_test(n):
    global m1, m2
    m1 = mertens(n)
    m2 = mertens(int(n ** 0.66666666666))
    assert(m1[-1] == mertens_extra(n, m2))


def mertens_test_test(n):
    for i in range(1, n, n // 7735 + 3):
        mertens_test(i)


def oo(n):
    for i in range(1, n):
        print(i, n // i, n // (n // i), n // (i + 1), n // (n // (i + 1)))


def totient_sum_buf(n, buf):
    nbuf = len(buf)
    s = 0
    n2 = int(sqrt(n))
    for i in range(1, n2 + 1):
        high = n // i
        low = n // (i + 1)

        k = (high - low) * (high + low + 1) // 2
        s += buf[i] * k
        ni = n // i

        if ni != i:
            if ni < nbuf:
                rec = buf[ni]
            else:
                rec = mertens_extra(ni, buf)
            s += rec * i
    return s


def totient_sum(n):
    n23 = int(n ** 0.6666666666) + 1
    buf = mertens(n23)
    return totient_sum_buf(n, buf)


def totient_sum_naive(n):
    return sum(primez.totient(i) for i in range(1, n + 1))


def blah(n):
    g = {}
    n2 = int(math.sqrt(n))
    for i in range(1, n2 + 1):
        g[i] = n // i - n // (i + 1)
        g[n // i] = 1
    return g


def testblah(n):
    for i in range(1, n):
        return foo(n) == blah(n)


def foo(n):
    g = {}
    for i in range(1, n + 1):
        ni = n // i
        g[ni] = g.get(ni, 0) + 1

    return g


def foo2(n):
    d = foo(n)
    for i, j in d.items():
        assert j == n // i - n // (i + 1)


def testfoo2(n, m=None):
    for i in range(1, n, m or 1):
        foo2(i)


def twofriends(n):
    n23 = int(n ** 0.6666666666) + 1
    buf = mertens(n23)
    s = 0
    while True:
        n //= 2
        s += (totient_sum(n) - 1)
        if n <= 1:
            return s


def twofriends_naive(n):
    s2 = set(2 ** i for i in range(1, 30))
    ret = 0
    print(s2)
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if gcd(i, j) in s2:
                ret += 1
    return ret
