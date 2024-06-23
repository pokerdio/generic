import primez


def gen(n):
    s = str(n)
    ndig = len(s)
    for i in range(1, 10):
        yield n + i * 10 ** ndig
    if ndig > 1 and s[1] != "0":
        yield int(s[1:])
    n2 = n
    maxten = 10 ** (ndig - 1)
    ten = 1
    while n2:
        dig = n2 % 10
        n2 //= 10
        for i in range(ten == maxten, dig):
            yield n - (dig - i) * ten
        for i in range(dig + 1, 10):
            yield n + (i - dig) * ten

        ten *= 10


def gen_smaller(n):
    s = str(n)
    ndig = len(s)
    maxten = 10 ** (ndig - 1)
    if ndig > 1 and s[1] != "0":
        yield int(s[1:])
    n2 = n
    ten = 1
    while n2:
        dig = n2 % 10
        n2 //= 10
        for i in range((ten == maxten), dig):
            yield n - (dig - i) * ten

        ten *= 10


def paint(p, set_primes, set_connected):
    op = {p}
    assert p not in set_connected and p in set_primes
    while op:
        p1 = op.pop()
        set_connected.add(p1)
        for p2 in gen(p1):
            if p2 < p and p2 in set_primes and p2 not in set_connected:
                op.add(p2)


def go(n):
    frend2 = {2}
    i = 0
    vp = list(primez.iterate_primez(n))[1:]
    sp = set(vp)

    retsum = 0
    for p in vp:
        for p2 in gen_smaller(p):
            if p2 in frend2:
                v.add(p)
                paint(p, sp, frend2)
                break
        else:
            retsum += p
    return retsum
