def kapow(n=10000, hope=maxhope()):
    v = {(2, 2)}
    v2 = set()
    ret = set()
    for i in range(n):
        c = min(v, key=lambda c: c[0] ** c[1])
        yield c
        v.remove(c)
        v2.add(c)
        c1, c2 = ((c[0] + 1), c[1]), (c[0], (c[1] + 1))
        if c1 not in v2:
            if c1[1] not in hope or hope[c1[1]] >= c1[0]:
                v.add(c1)
        if c2 not in v2:
            if c2[1] not in hope or hope[c2[1]] >= c2[0]:
                v.add(c2)


def digisum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def go(n=1000):
    k = 0
    for a, b in kapow(n):
        if digisum(a ** b) == a:
            k += 1
            print(a ** b, k)


def maxhope(n=100):
    ret = {}
    for nines in range(1, n):
        for first_digit in range(1, 10):
            k = (first_digit + 1) * 10 ** nines - 1

            for p in range(2, 100):
                if digisum(k) ** p < k and p not in ret:
                    ret[p] = digisum(k)

    return ret
