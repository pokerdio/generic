import primez


def tenmax(p):
    ret = 1
    while ret < p:
        ret *= 10
    return ret


def foo(p1, p2):
    assert(p2 > 5)

    p = p1
    delta = tenmax(p1)
    k = 0
    while True:
        p = (p + delta) % p2
        k = k + 1
        if p == 0:
            return k * delta + p1


def go(n=1000000):
    g = primez.iterate_primez()
    next(g)
    next(g)
    p1 = next(g)
    assert(5 == p1)

    s = 0
    k = 0
    while p1 <= n:
        p2 = next(g)
        if p1 // (n // 100) > k:
            k = p1 // (n // 100)
            print("%d%%" % (p1 // (n // 100)), p1, p2)

        s += foo(p1, p2)

        p1 = p2
    return s
