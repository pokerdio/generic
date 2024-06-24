from fractions import Fraction as Fr


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


def invp(a, p):
    """p is prime plox - so I can invert a mod p """
    one, s, t = ee(a, p)
    assert(one == 1)
    return (s % p)


def Q(a, b, p):
    return ((invp(b, p)) * a) % p


# def vv(v1, v2):
#     return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]


# def mm(m1, m2):
#     return [vv(m1[0:3], m2[0::3]), vv(m1[0:3], m2[1::3]), vv(m1[0:3], m2[2::3]),
#             vv(m1[3:6], m2[0::3]), vv(m1[3:6], m2[1::3]), vv(m1[3:6], m2[2::3]),
#             vv(m1[6:9], m2[0::3]), vv(m1[6:9], m2[1::3]), vv(m1[6:9], m2[2::3])]


# def mv(m, v):
#     return [vv(m[0:3], v), vv(m[3:6], v), vv(m[6:9], v)]


def vv(v1, v2, p):
    return (v1[0] * v2[0] + v1[1] * v2[1]) % p


def mm(m1, m2, p):
    return [vv(m1[0:2], m2[0::2], p) % p, vv(m1[0:2], m2[1::2], p) % p,
            vv(m1[2:], m2[0::2], p) % p, vv(m1[2:], m2[1::2], p) % p]


def mv(m, v, p):
    return [vv(m[0:2], v, p) % p, vv(m[2:], v, p) % p]


def mpow(m, k, p):
    two = 2
    mpow = [m]
    while two <= k:
        mpow.append(mm(mpow[-1], mpow[-1], p))
        two *= 2
    ret = (1, 0, 0, 1)
    i, two = 0, 1
    while two <= k:
        if two & k:
            ret = mm(ret, mpow[i], p)
        i += 1
        two *= 2
    return ret


def invm(m, p):
    det = m[0] * m[3] - m[1] * m[2]
    return [Q(m[3], det, p), -Q(m[1], det, p), -Q(m[2], det, p), Q(m[0], det, p)]


def go(n, p=1000000009):
    m = (0,) + (Q(1, 2, p),) * 3
    v0 = (Q(1, 4, p), ) * 2

    m0 = mpow(m, n - 3, p)
    m3 = mpow(m, 3, p)
    mn = mm(m0, m3, p)
    mtot = mm(invm([1-mn[0], -mn[1], -mn[2], 1-mn[3]], p), m0, p)
    vret = mv(mtot, v0, p)

    return Q(vret[1], 2, p)


# HT 1/4
# TT 1/4
# TH 1/4

# HT2 = TH / 2
# TT2 = HT / 2 + TT / 2
# TH2 = HT / 2 + TT / 2

# therefore tt and th are always =
# therefore:

# HT=TH/2
# TH=HT/2+TH/2


# m0 = m**n-3
# mr = m ** n
# v = m0 * v0 + mr * m0  * v0 + mr**2 * m0 * v0 + ...


# (1+mr+mr**2+...) * m0 * v0

# s = 1+mr+...
# s mr = mr+....
# s(1 - mr) = 1
# s = inv(1-mr)


print(go(10**18, 1000000009))
