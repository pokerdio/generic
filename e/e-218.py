def _pow(x, e, n):
    ret = 1
    for i in range(e):
        ret = (ret * x) % n
    return ret


def _p(n):
    for e in range(2, n):
        if gcd(e, n) == 1:
            print(f"e={e}  " + " ".join(f"{x}->{_pow(x, e, n)}" for x in range(1, n)))


def _ones_gen(n):
    for e in range(2, n):
        if gcd(e, n) == 1:
            yield e, sum(1 == _pow(x, e, n) for x in range(1, n))


def _ones(n, min=min):
    ret = list(_ones_gen(n))
    min_ones = min(ret, key=lambda x: x[1])[1]
    return min_ones, list(x[0] for x in ret if x[1] == min_ones)


def foo(n, min=min):
    for n in range(4, n):
        print(n, *_ones(n, min))


def foo(n):
    for i in range(2, n + 1):
        s = "%dth power: " % i
        s += " ".join("%d->%d" % (j, (j ** i) % n) for j in range(1, n) if gcd(j, n) == 1) + " "
        s += " ".join("%d(%d)->%d" % (j, gcd(j, n), (j ** i) % n) for j in range(1, n) if gcd(j, n) > 1)
        print(s)
