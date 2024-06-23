import random


def solo_ev(m, n):
    """ev of square of number of orders taking number of still drones from
    m to m-1"""
    p = m / n  # chance of a still drone being activated
    pass


# 1: p
# 2: 4 * (1-p) * p
# 3: 9 * (1-p) ^ 2 * p
# 4: 16 * (1-p) ^ 3 * p

def foo(p):
    p1 = 1.0
    s = 0.0
    for i in range(1, 100):
        s += p * p1 * i * i
        p1 *= 1 - p
    return s


# p
# (1-p)p
# (1-p) ^ 2p
# .....
# --------
# 1.0


# 3 * (1 - p) * p
# 3 * (1 - p) ^ 2 * p
# 3 * (1 - p) * p
# .......
# -----------
# 3 * (1-p)

# ....

# 1
# 3 * (1 - p)
# 5 * (1 - p) ^ 2
# ..............

def foo(p):
    s = 0
    p1 = 1.0
    for i in range(100):
        s += (i * 2 + 1) * p1
        p1 *= 1 - p
    return s


# 1/p + 2 * (1 - p)/p + 2 * (1 - p) ^ 2/p + ...
# 1/p + 2*(1-p)/p / p

def foo(p):
    return 1 / p + 2 * (1 - p) / p / p


def solo_mc(m, n):
    ret = 1
    while random.randint(1, n) > m:
        ret += 1
    return ret ** 2


def foo_solo(m, n):
    k = 1000000
    ret = 0
    for i in range(k):
        ret += solo_mc(m, n)
    return ret / k


def solo(m, n):
    p = m / n
# 1/p + 2*(1-p) / (p * p)
    return 1/p + 2 * (1 - p) / (p ** 2)


def go(n):
    s = 0.0
    for i in range(1, n + 1):
        s += n / i

    s2 = 0.0
    for i in range(1, n + 1):
        ev = n / i
        p = i / n
        s2 += ev * s - ev * ev + ev + 2 * (1 - p) * ev * ev
    return (s2 + s) / 2.0 / n


def mc(n):
    rest = n
    tries = 0
    while rest > 0:
        if random.randint(1, n) <= rest:
            rest -= 1
        tries += 1
    return tries


def mc2(n):
    rest = n
    drone_speed = 0
    total_dist = 0
    while rest > 0:
        if random.randint(1, n) <= rest:
            rest -= 1
        drone_speed += 1
        total_dist += drone_speed
    return total_dist


def triangle(n):
    return n * (n + 1) / 2


def foo(n, k=100000):
    total = 0
    for i in range(k):
        total += mc2(n)
    return total / k / n


def foo2(n):
    ret = 0
    for i in range(1, n + 1):
        ret += n / i
    return ret
