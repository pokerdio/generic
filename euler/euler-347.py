import primez


def gopair(p, q, n):
    max = p * q
    assert(max <= n)
    pmax = q

    while pmax * p <= n:
        pmax *= p

        pqmax = pmax
        while pqmax * q <= n:
            pqmax *= q
        if pqmax > max:
            max = pqmax
    return max


def go(n):
    vp = list(primez.iterate_primez(n + 10))
    ret = 0
    for i in range(len(vp) - 1):
        pi = vp[i]
        for j in range(i + 1, len(vp)):
            pj = vp[j]
            if pi * pj > n:
                break
            ret += gopair(vp[i], vp[j], n)
    return ret
