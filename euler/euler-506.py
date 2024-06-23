from builtins import sum


def gen():
    for _ in range(100):
        for i in (1, 2, 3, 4, 3, 2):
            yield i


def foo():
    g = gen()
    repeater = 123432
    for i in range(1, 16):
        x, y = 0, 0
        disrep = repeater
        while x < i:
            digit = next(g)
            repeater = (repeater - (repeater // 100000) * 100000) * 10 + (repeater // 100000)
            x = x + digit
            y = y * 10 + digit
        yield i, y, disrep


def go(n, mod=123454321):
    ret = 0
    for i, y, repeater in foo():
        count = (n - i) // 15
        if count >= 0:
            r = rep(repeater, count, mod)
            ret += (r * (10 ** len(str(y))) + (y * (count + 1))) % mod
    ret %= mod
    return ret


def rep(n0, count, mod):
    n0 %= mod
    v = [n0]
    s = {n0}
    ten = 10 ** len(str(n0))
    while True:
        n1 = (v[-1] * ten + n0) % mod
        if n1 in s:
            assert(v.index(n1) == 0)
            return (sum(v) * (count // len(v)) + sum(v[:count % len(v)])) % mod
        s.add(n1)
        v.append(n1)


print(go(10**14))
