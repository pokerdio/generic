def d(n, base):
    s = 0
    while n > 0:
        s += n % base
        n //= base
    return s


def go(n, k, l):
    assert(1 <= k < l)

    k = 2 ** k
    l = 2 ** l

    d = {}

    for i in range(l):
        pass
