def ee(a, b):
    """function extended_gcd(a, b)"""
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)

    while r > 0:
        quotient = old_r // r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)

    # print("Bézout coefficients:", (old_s, old_t))
    # print("greatest common divisor:", old_r)
    # print("bezout value (should equal the gcd):", old_s * a + old_t * b)
    # print("quotients by the gcd:", (t, s))
    return old_r, old_s, old_t


def invp(a, p=1000000007):
    """p is prime plox - so I can invert a mod p """
    if a == 0:
        return 0
    one, s, t = ee(a, p)
    return (s % p)


def initC(n):
    ret = [[1, ], [1, 1]]
    for i in range(2, n + 1):
        v = [1] * (i + 1)
        for j in range(1, i):
            v.append((ret[i - 1][j - 1] + ret[i - 1][j]) % 1000000007)
        ret.append(v)
    return ret


def C(n, inv=[invp(x) for x in range(0, 10**5+5)]):
    yield 1
    ret = 1
    for i in range(1, n + 1):
        ret = ((n + 1 - i) * ret) % 1000000007
        ret = (ret * inv[i]) % 1000000007
        yield ret


def total_combos(n):
    ret = 0
    for c in C(n):
        ret += kapow(c, 16)
    if n % 100 == 0:
        print(n)
    return ret % 1000000007


def kapow(a, b, p=1000000007):
    ret = 1

    while b > 0:
        if b % 2 == 1:
            ret = (ret * a) % p
        a = a * a % p
        b //= 2
    return ret


def go(n, m):
    assert(m % n == 0)
    m //= n
    tc = [total_combos(n) for n in range(2, n + 1)]
    tc.insert(0, 0)
    tc.insert(0, 1)
    twos = [1]
    for i in range(n):
        twos.append((twos[-1] * 2) % 1000000007)
    for i in range(2, n + 1):
        if i % 100 == 0:
            print(i)
        c = C(i)
        next(c)
        for z in range(1, i + 1):
            tc[i] = (tc[i] - tc[i - z] * twos[z] * next(c)) % 1000000007
    ret = 0
    c = C(n)
    for i in range(0, n + 1):

        ret = (ret + tc[i] * kapow(2, m * (n - i), 1000000007) * next(c)) % 1000000007
    return ret


print(go(10**5, 10**16))
