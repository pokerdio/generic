import primez


def foo(p):
    r = 1111111111 % p
    ten = 10000000000 % p
    if r == 0:
        return
    v = {r}

    while True:
        r2 = 0
        for i in range(10):
            r2 += r * (ten ** i) % p
        ten = (ten ** 10) % p
        r2 %= p
        if r2 == 0:
            return
        if r2 in v:
            return True
        v.add(r2)
        r = r2


def go(n=100):
    s = 0
    for i in primez.iterate_primez(n):
        if foo(i):
            s += i
    return s


def r(n):
    return int("1" * n)


def go2(n=100):
    for i in primez.iterate_primez(n):
        if foo(i):
            print(i - 1)
