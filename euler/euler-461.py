def f(n, k):
    return e ** (k / n) - 1


def g(n, a, b, c, d):
    ret = 0.0
    for k in (a, b, c, d):
        ret += f(n, k)
    return abs(ret - math.pi)


def step(n, a0, b0, c0, d0):
    ret = None
    bestg = g(n, a0, b0, c0, d0)
    plus, minus = 25, 25
    for a in range(a0 - minus, a0 + plus):
        for b in range(b0 - minus, b0 + plus):
            for c in range(c0 - minus, c0 + plus):
                for d in range(d0 - minus, d0 + plus):
                    g1 = g(n, a, b, c, d)
                    if g1 < bestg:
                        bestg = g1
                        ret = (a, b, c, d)
    return ret


def go(n, a0, b0, c0, d0):
    for _ in range(1000):
        print(_ % 2 and "ping" or "pong")
        ret = step(n, a0, b0, c0, d0)
        if ret:
            a0, b0, c0, d0 = ret
        else:
            return a0, b0, c0, d0
    return a0, b0, c0, d0


def main():
    a, b, c, d = go(10000, 50 * 6, 50 * 75, 50 * 89, 50 * 226)

    print(g(10000, a, b, c, d), a, b, c, d)

    return a ** 2 + b ** 2 + c ** 2 + d ** 2
