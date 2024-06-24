from math import sqrt
import time
# def foo(p, q):
#     s = ""
#     for x in range(1, n):
#         s += f"{x:2},{x%p:2},{x%q:2},{x % p % q:2},{x % q % p:2}"


def sieve(n, store=[10, [3, 5, 7]]):
    v = store[1]
    if store[0] == n:
        return v
    if store[0] > n:
        for i in range(len(v)):
            if v[i] > n:
                return v[:i]
            if v[i] == n:
                return v[:i + 1]

    store[0] = n
    sv = [True] * (n + 1)
    for i in range(2, int(sqrt(n)) + 2):
        if sv[i]:
            for j in range(i * 2, n + 1, i):
                sv[j] = False

    store[1] = [x for x in range(2, n + 1) if sv[x]]
    return store[1]


def two_digitz(n):
    ret = 0
    while n > 0:
        n //= 2
        ret += 1
    return ret


def foo(p, count=[0]):
    count[0] += 1
    if count[0] > 1000:
        count[0] = 0
        print("doing ", p)

    if p <= 2:
        return 0
    smallest_pete = p + two_digitz(p) + 1

    k = 1
    period = 0
    if not count[0]:
        time0 = time.time()

    while True:
        k *= 2
        k %= p
        period += 1
        if k == 1:
            break

    if not count[0]:
        timea = time.time()
    p2 = 2 ** p
    newp = p2 % period + ((smallest_pete + period - 1) // period) * period
    if not count[0]:
        print("period", period, "digitz", newp, p)
        timeb = time.time()

    ret = ((2 ** newp) // p) % p2 % p
    if not count[0]:
        timec = time.time()
        print("times:", timea-time0, timeb-timea, timec-timeb)

    return ret


def foo2(p, count=[0]):
    count[0] += 1
    if count[0] > 1000:
        count[0] = 0
        print("doing ", p)

    if p <= 2:
        return 0
    smallest_pete = p + two_digitz(p) + 1

    k = 1
    period = 0
    if not count[0]:
        time0 = time.time()
    period = p - 1
    if not count[0]:
        timea = time.time()
    p2 = 2 ** p
    newp = p2 % period + ((smallest_pete + period - 1) // period) * period
    if not count[0]:
        print("period", period, "digitz", newp, p)
        timeb = time.time()

    ret = (((2 ** newp) // p) & (p2 - 1)) % p
    if not count[0]:
        timec = time.time()
        print("times:", timea-time0, timeb-timea, timec-timeb)

    return ret


def bar2(n):
    return sum(foo2(x) for x in sieve(n))


def bar(n):
    return sum(foo(x) for x in sieve(n))


# print(bar2(10**7))
# 1603036763131
