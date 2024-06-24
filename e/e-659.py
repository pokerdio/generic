import primez


def foo(n=1000):
    for i in range(1, n + 1):
        k = 4 * i * i + 1
        dec = primez.decompose(k)
        p = max(dec)
        for c in range(1, n, 2):
            nn = (2 * c + 1) * p // 2
            if (nn * nn + i * i) % p == 0:
                print("success ", i, k, p, c, dec)
                break
        else:
            print("fail", i)


def bar(n=50):
    return sum(max(primez.decompose(i * i * 4 + 1)) for i in range(1, n + 1))


def boo(p, n=1000):

    last = 0
    for i in range(1, n):
        k = 4 * i * i + 1
        d = primez.decompose(k)
        if p in d:
            print(i - last, i, k, p, d)
            last = i


def go2(n):
    v = list(range(n + 1))
    it = primez.iterate_primez(n * 100)
    for _ in range(n):
        p = next(it)
    k = 5 % p
    delta = 12 % p
    v = []
    s = set()
    while True:
        pair = (k, delta)
        if pair in s:
            return (p, v.index(pair), len(v), v)
            break
        v.append(pair)
        s.add(pair)
        k = (k + delta) % p
        delta = (8 + delta) % p


def foo(p):
    for i in range(1000):
        k = 4 * i * i + 1
        if k % p == 0:
            yield i


def dif(it):
    k = None
    for i in it:
        if k:
            yield i - k
        k = i


def foo(p):
    g = {}
    start = 1
    delta = 4
    k = 0
    ret = []
    while (start, delta) not in g:
        g[start, delta] = k
        start = (start + delta) % p
        delta = (delta + 8) % p
        k = k + 1
    assert (k == p)
    return [x for r, x in g.items() if r[0] == 0]


def foo2(p):
    if p % 4 == 3:
        return None
    start = 1
    delta = 4
    k = 0
    while True:
        if start == 0:
            return (k, p - k)
        start = (start + delta) % p
        delta = (delta + 8) % p
        k = k + 1


def maxdiv(n, vp, i0):
    factors = {}
    ret = n
    for i in range(i0, len(vp)):
        p = vp[i]
        while n % p == 0:
            n //= p
            ret = p
        if n == 1 or p * p > n:
            break
    return max(n, ret)


def go0(n=10 ** 7):
    vp = [p for p in primez.iterate_primez(2 * n) if p % 4 == 1]
    kp = [4 * i * i + 1 for i in range(0, n + 1)]
    maxp = [0] * (n + 1)

    prime_limit = len(vp) // 7

    print(len(vp), vp[prime_limit])
#    print(vp[:prime_limit])
    count = 0

    for p in vp[:prime_limit]:
        cy = foo2(p)
        count += 1
        if count % 100 == 0:
            print(p, cy)
        for dp in cy:
            for i in range(dp, n + 1, p):
                assert(kp[i] % p == 0)
                while kp[i] % p == 0:
                    kp[i] //= p
                maxp[i] = p

    s = 0
    for i in range(1, n + 1):
        if i % 10000 == 00:
            print(i, kp[i])
        if kp[i] == 1:
            s += maxp[i]
            continue
        if primez.rm_prime(kp[i], 22):
            maxp[i] = max(kp[i], maxp[i])
            s += maxp[i]
            continue
        dd = maxdiv(kp[i], vp, prime_limit)
        # if dd != max(primez.decompose(kp[i])):
        #     print(i, kp[i], maxp[i], dd, primez.decompose(kp[i]))
        #     assert(False)
        maxp[i] = max(dd, maxp[i])
        s += maxp[i]
    return s, maxp


def test(n):
    s = 0
    maxp = [0] * (n + 1)
    for i in range(1, n + 1):
        maxp[i] = max(primez.decompose(i * i * 4 + 1))
        s += maxp[i]
    return s, maxp


def foo(n):
    for p in primez.iterate_primez(n):
        print(p, len(set(i * i % p for i in range(p))))


def foo(n):
    for p in primez.iterate_primez(n):
        s = sorted(list(set(i * i % p for i in range(1, p // 2 + 1))))
        print(p, s)
        print("".join("(%d %d) - " % (i, (i ** (p // 2)) % p) for i in range(1, p))[:-3])


def foo(n):
    return [pow(i, n - 1, n) for i in range(1, n)]


def residueset(p):
    return set(i * i % p for i in range(1, p))


def isresidue(a, p):
    """p is  an odd prime"""
    return pow(a, p // 2, p) == 1


    return [(i, pow(i, p // 2, p)) for i in range(1, p)]


def fermat_list(p):
    return [pow(i, p - 1, p) for i in range(1, p)]


def sqrt34(a, p):
    if p % 4 == 3:
        if isresidue(a, p):
            return pow(a, (p + 1) // 4, p)


def tonelli_shanks(a, p):
    p1 = p - 1
    p12 = p1 // 2
    if a == 0:
        return (0,)
    if pow(a, p12, p) == p1:
        return tuple()

    assert(pow(a, p12, p) == 1)

    q, s = p1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    for i in range(2, p):
        if pow(i, p12, p) == p1:
            z = i
            break
    else:
        assert False, "wtf"

    r = pow(a, (q + 1) // 2, p)
    t = pow(a, q, p)
    m = s

    c = pow(z, q, p)

#    print("0 q=%d s=%d n=%d p=%d z=%d c=%d r=%d t=%d" % (q, s, a, p, z, c, r, t))

    while True:
        if t == 1:
            return r, p - r

        t2 = t
        for i in range(1, m):
            t2 = t2 * t2 % p
            if t2 == 1:
                break
        else:
            assert False, "goddamnit"
        assert m >= i + 1, ("tonelli", a, p, i, m)
        b = pow(c, 2 ** (m - i - 1), p)
        r = r * b % p
        t = t * b * b % p
        c = b * b % p
        m = i
#        print("brtcm", b, r, t, c, m)


def go(n=10 ** 7):
    vp = [p for p in primez.iterate_primez(2 * n) if p % 4 == 1]
    kp = [4 * i * i + 1 for i in range(0, n + 1)]
    maxp = [0] * (n + 1)

    prime_limit = len(vp) // 7

    print(len(vp), vp[prime_limit])
#    print(vp[:prime_limit])
    count = 0

    for p in vp:
        root = tonelli_shanks(p - 1, p)
        if not root:
            continue
        root = ((root[0] % 2 == 0) and root[0] or root[1]) // 2
        for r in (root, p - root):
            for i in range(r, n + 1, p):
                assert kp[i] % p == 0, (kp[i], i, p)
                while kp[i] % p == 0:
                    kp[i] //= p
                    maxp[i] = p

    s = 0
    print("stage two")
    for i in range(1, n + 1):
        if i % 10000 == 00:
            print(i, kp[i])
        if kp[i] == 1:
            s += maxp[i]
        else:
            s += kp[i]

    return s % 10 ** 18
