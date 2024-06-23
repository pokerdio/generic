import sieves as sv
import mathmath as mm


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


def invp(a, p=1004535809):
    """p is prime plox - so I can invert a mod p """
    one, s, t = ee(a, p)
    assert(one == 1)
    return (s % p)


def go(n, mod=1004535809):
    vp = [1] + list(sv.sieve_atkin(n * 35))[:n]
    vp = [vp[i + 1] - vp[i] for i in range(n)]

    return vp
    v = [1] * n
    for big in range(2, n):
        v2 = v.copy()

        combo = 1
        for j in range(1, n // big + 1):
            pass
    return vp


# pi(1) = 0
# pi(2) = 1
# pi(3) = 2
# pi(4) = 2
# pi(5) = 3

# t(3,3)=19
# t(10,10) = 869985
# t(1000,1000) = 578270566 (mod 1004535809)


def pc(n, mod=1004535809):
    """counts partition counts up to n by largest partioned element"""
    v = [1] * (n + 1)
    ret = [0, 1]
    for big in range(2, n + 1):
        print(big)
        v2 = v.copy()
        for k in range(big, n + 1, big):
            for i in range(n - k + 1):
                v2[k + i] += v[i]
        v = [x % mod for x in v2]
        ret.append(v[-1])
    return [ret[i + 1] - ret[i] for i in range(n)]


def go(n=20000):
    v = pc(n)
