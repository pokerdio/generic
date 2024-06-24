from builtins import sum


def pow(matrix, n, x):
    v = []
    while n > 0:
        if n % 2 == 0:
            n //= 2
            matrix = mul22(matrix, matrix, x)
        else:
            v.append(matrix)
            n -= 1
    ret = v[0]
    for i in range(1, len(v)):
        ret = mul22(ret, v[i], x)
    return ret


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def rev(n, mod):
    _, x, _ = egcd(n, mod)
    return x % mod


def f(n=10, a0=0):
    a1 = 1
    for _ in range(n):
        yield a1
        a0, a1 = a1, 6 * a0 + 2 * a1


def foo(n):
    a, b = 1, 1
    for i in range(1, n * n):
        if a == 1 and b == 0:
            print(i, n)
            return i
        a, b = (a + b * 7) % n, (a + b) % n
    return 0


def go(n):
    s = 0
    for i in range(2, n + 1):
        if i % 2 == 1 and i % 3 > 0:
            s += foo(i)
    return s


def mul22v(m, v, x):
    a = m[0] * v[0] + m[1] * v[1]
    b = m[2] * v[0] + m[3] * v[1]
    return (a % x, b % x)


def mul22(m1, m2, x):
    a = m1[0] * m2[0] + m1[1] * m2[2]
    b = m1[0] * m2[1] + m1[1] * m2[3]
    c = m1[2] * m2[0] + m1[3] * m2[2]
    d = m1[2] * m2[1] + m1[3] * m2[3]

    return (a % x, b % x, c % x, d % x)


def inverse22(m, x):
    a, b, c, d = m
    """inverse mod x of ((a,b),(c,d))"""
    det = rev((a * d - b * c) % x, x)
    if det:
        return (d * det % x, -b * det % x, -c * det % x, a * det % x)


def foo2(x):
    m = (1, 7, 1, 1)

    v = (1, 1)

    d = {v: 0}

    for i in range(1, x):
        v = mul22v(m, v, x)
        if v == (1, 0):
            return i
        d[v] = i

    m1 = pow(inverse22(m, x), x, x)
    m1 = (m1[0][0], m1[0][1], m1[1][0], m1[1][1])

    v2 = (1, 0)

    for i in range(1, x):
        v2 = mul22v(m1, v2, x)
        if v2 in d:
            return i * x + d[v2]


def foo3(x):
    m = (1, 7, 1, 1)
    v = (1, 1)

    dic = {v: 0}

    a, b = 1, 1
    for i in range(1, x):
        a, b = ((a + 7 * b) % x, (a + b) % x)
        v = (a, b)
        if v == (1, 0):
            return i
        dic[v] = i

    if (1, 0) in dic:
        return dic[(1, 0)]

    (a, b, c, d) = pow(inverse22(m, x), x, x)
    v2a, v2b = (1, 0)

    for i in range(1, x):
        v2a, v2b = ((a * v2a + b * v2b) % x), ((c * v2a + d * v2b) % x)
        if (v2a, v2b) in dic:
            return i * x + dic[(v2a, v2b)]


def go2(n):
    s = 0
    for i in range(2, n + 1):
        if i % 1000 == 1:
            print(i)
        if i % 2 == 1 and i % 3 > 0:
            s += foo3(i) + 1
    return s


# print(go2(10**3))
