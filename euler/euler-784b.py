from math import gcd
from itertools import product
from functools import reduce
from operator import mul


import primez


def gen_primez(n):
    v = [1] * (n)
    ret = []
    for i in range(2, n):
        if v[i]:
            for j in range(i, n, i):
                v[j] = 0
            ret.append(i)
    return ret


#primez = gen_primez(2005000)


def make_inv(n):
    inv = [{} for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i):
            for k in range(2, n + 1):
                if i * j % k == 1:
                    inv[k][i] = j % k
                    inv[k][j] = i % k
    return inv


def foo(n=100):
    inv = make_inv(n)
    ret = []
    for i in range(1, n + 1):
        for j in range(1, i):
            if i not in inv[j] or j not in inv[i]:
                continue
            if inv[j][i] == inv[i][j]:
                ret.append((j, i, inv[i][j]))
    return set(ret)


x = 5

# r * q == 1 mod p
# r * p == 1 mod q

# r * q = p * k + 1
# r * p = q * t + 1


# r*q -r*p = p*k - q*t
# (r+t)*q = (k+r)*p

# p = r+t; q=k+r

# r*q = p*(q-r) + 1
# r(q+p) = p*q + 1


# -----
# 2 * 3 == 5 * 1 + 1
# 2 * 5 == 3 * 3 + 1
# (2+3)*3==(1+2)*5


def bar(n=100):
    v = foo(n)
    for p, q, r in v:
        k = r * q // p
        t = r * p // q
        if (p * q + 1) // (p + q) != r:
            print("oh no")
        #print(p, q, "-", r, (p * q + 1) // (p + q), "-", k, t, "-", r + k, r + t)


# p*q+1 = r * (p + q)
# (p+1)(q+1) - p - q = r*(p+q)

# (p+1)(q+1) = (r+1)(p+q)

def go(n=100):
    for s in range(2, n):
        s21 = s * s + 1


def gah(n=10):
    for i in range(2, n + 1):
        print(i, i * i + 1, primez.decompose(i * i + 1))


foobar = 666


def goo():
    print(f"{foobar}")


def foo2(n=100):
    ret = []
    for i in range(2, n):
        for j in range(i + 1, n + 1):
            if (i * j + 1) % (i + j) == 0:
                r = (i * j + 1) // (i + j)
                print(gcd(i + 1, j + 1), i + 1, primez.decompose(i + 1), j +
                      1, primez.decompose(j + 1), i+j, primez.decompose(i + j))


def p_content(x, p):
    if x == 0:
        return 999
    ret = 0
    while x % p == 0:
        x //= p
        ret += 1
    return ret


def go(a):
    assert(a > 1)
    # two
    two = []
    if a % 2 == 1:
        s = 1
        s2 = 0
        a2 = p_content(a + 1, 2)
        while p_content(s - a + 1, 2) + a2 >= s2:
            two.append(s)
            s = s * 2
            s2 = s2 + 1
        print("two s", two)

    # non-two primez that divide a
    d = primez.decompose(a + 1)
    if 2 in d:
        del d[2]
    a_divz = []

    for p, ppow in d.items():
        a_divz.append(list(p ** x for x in range(ppow + 1)))
        print("b", p, a_divz[-1])

    b_divz = []
    for p in primez.iterate_primez(a + 5):
        if p == 2:
            continue
        v = []
        for ppow in range(1, 100):
            if a % (p ** ppow) != 1:
                break
            v.append(p ** ppow)
        if v:
            b_divz.append([1, *v])
            print("c", p, b_divz[-1])

    v = a_divz + b_divz
    if two:
        v = [two] + v
    print("final ending", v)
    ret = 0
    for c in product(*v):
        s = reduce(mul, c, 1)
        b = s - a
        if b > a:
            ret += (a + b)
    return ret


def go2(a):
    assert(a > 1)
    # two
    two = []
    if a % 2 == 1:
        s = 1
        s2 = 0
        a2 = p_content(a + 1, 2)
        while p_content(s - a + 1, 2) + a2 >= s2:
            two.append(s)
            s = s * 2
            s2 = s2 + 1

    # non-two primez that divide a
    d = primez.decompose(a + 1)
    if 2 in d:
        del d[2]
    a_divz = []

    for p, ppow in d.items():
        a_divz.append(list(p ** x for x in range(ppow + 1)))

    b_divz = []
    for p in primez.iterate_primez(a + 5):
        if p == 2:
            continue
        v = []
        for ppow in range(1, 100):
            if a % (p ** ppow) != 1:
                break
            v.append(p ** ppow)
        if v:
            b_divz.append([1, *v])

    v = a_divz + b_divz
    if two:
        v = [two] + v
    ret = 0
    for c in product(*v):
        s = reduce(mul, c, 1)
        b = s - a
        if b > a:
            ret += (a + b)
    return ret


def F(n):
    ret = 0
    for x in range(2, n + 1):
        ret += go(x)
        if x % 1000 == 1:
            print(x)
    return ret


# print(F(2000000))
