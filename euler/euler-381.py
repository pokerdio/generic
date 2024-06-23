import primez


def xeuler(m, n):
    v = []
    assert(m >= n)
    if m % n == 0:
        return 0, 1, n
    while (True):

        c, r = m // n, m % n
        if r == 0:
            r = n  # the cmmdc
            break
        v.append((m, n, c))
        m, n = n, r

    a, b = 1, -v[-1][2]
    for m, n, c in v[-2::-1]:
        #        m = n * c + z
        #        a * n + b * z = r

        a, b = b, a - b * c
    return a, b, r


def foo(p):
    ret = p - 1
    rev = p - 1
    for p1 in range(p - 1, p - 5, -1):
        a, b, _ = xeuler(p, p1)
        rev = rev * b % p

        ret += rev

    return ret % p


def go(n):
    s = 0
    for p in primez.iterate_primez(n):
        if p >= 5:
            s += foo(p)
    return s
