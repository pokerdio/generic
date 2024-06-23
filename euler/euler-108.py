import primez


def kapow(n, top, s=()):
    if n == 0:
        yield s
        return
    for i in range(0, top + 1):
        yield from kapow(n - 1, i, (*s, i))


def count_mn(prime_powers):
    ret = 1
    for k in prime_powers:
        ret *= (2 * k + 1)
    return (ret + 1) // 2


def go(n, top, threshold=1000):
    ret = None
    for combo in kapow(n, top):
        value = count_mn(combo)
        if value > threshold:
            zed = prod_pow(combo)
            ret = min(ret or zed, zed)
    return ret


def prod_pow(prime_powers):
    ret = 1
    for i in range(len(prime_powers)):
        ret *= (primez.primez[i] ** prime_powers[i])
    return ret
