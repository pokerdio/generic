import primez


def signatures(vp, start, m, n):
    for i in range(start, len(vp)):
        p = vp[i]
        p3 = p ** 3
        if p3 * m > n:
            return
        yield (p,)
        for combo in signatures(vp, i + 1, m * p3, n):
            yield (p, *combo)


def signatures_go(n):
    n3 = int(n ** 0.333334) + 2
    return list(signatures(list(primez.iterate_primez(n3)), 0, 1, n))


def signature_grow(s, n, m=0):
    if not m:
        m = 1
        for i in s:
            m *= (i ** 3)
    if len(s) == 1:
        while m <= n:
            yield m
            m = m * s[0]
    else:

        s2 = s[1:]
        while m <= n:
            yield from signature_grow(s2, n, m)
            m = m * s[0]


def go(n):
    ret = 0
    for sig in signatures_go(n):
        for m in signature_grow(sig, n):
            ret += n // m
    return ret + n


# go(10**18) > > 1339784153569958487
