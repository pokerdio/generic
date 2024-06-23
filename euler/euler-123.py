import primez


def powmod(p, m, mod):
    ret = (p ** (m % 10)) % mod
    if m >= 10:
        ret = powmod(p ** 10 % mod, m // 10, mod) * ret % mod
    return ret


def powmodtest(p, m, mod):
    return p ** m % mod


def test_powmod():
    for i in range(1000):
        p = randint(2, 1000)
        m = randint(2, 1000)
        mod = randint(50, 150)
        assert(powmod(p, m, mod) == powmodtest(p, m, mod))


def go(n=1000000, thresh=10**9):
    k = 0
    for p in primez.iterate_primez(n):
        k += 1
        sq = p * p
        r = (powmod(p - 1, k, sq) + powmod(p + 1, k, sq)) % sq
        if r > thresh:
            return p, k
