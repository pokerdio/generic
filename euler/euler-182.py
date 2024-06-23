import primez


def decomp(n, d={}):
    if n not in d:
        d[n] = primez.decompose(n)
    return d[n]


def f(n):
    ret = [12]
    v = [1] * n
    for e in range(n - 2):
        ones = 0
        for i in range(n):
            v[i] = (v[i] * i) % n
            if v[i] == 1:
                ones += 1
        ret.append(ones)
    return ret


def go(p, q):
    vp = f(p)
    vq = f(q)
    n = p * q
    phi = (p - 1) * (q - 1)

    v = []

    min_ones = p * q
    for e in range(1, phi - 1):
        if gcd(e + 1, phi) == 1:
            f1 = vp[e % (p - 1)]
            f2 = vq[e % (q - 1)]
            ones = f1 * f2
            if ones < min_ones:
                min_ones = ones
            v.append((e, ones))
    print("ones", min_ones)
    return sum(e + 1 for e, ones in v if ones == min_ones)


def foo(p, q, e):
    n = p * q
    v = list(range(n))
    ret = []
    for _ in range(e - 1):
        for i in range(n):
            v[i] = v[i] * i % n
        s = sum(1 for x in v if x == 1)
        if s == 1:
            ret.append(_ + 2)
            print(_ + 2, s)
    return ret
