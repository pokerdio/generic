def foo(n):
    for i in range(1, n):
        j = n * n // i
        for k in range(max(1, j - 5), j + 5):
            if abs(n * n - i * k) <= 2:
                yield (n, i, k)


def go(n):
    s = set()
    for i in range(1, n + 1):
        for _, a, b in foo(i):
            s.add((a, b))
    return s


def step(a, b):
    c = b * b // a
    for k in range(max(1, c - 3), c + 3):
        if abs(b * b - a * k) <= 2:
            return k


def steps(a, b, n=10):
    ret = [a, b]
    for i in range(n):
        a, b = b, step(a, b)
        if not b:
            return ret
        ret.append(b)
    return ret


def actually_geo(s):
    for a, b, c in zip(s[:-2], s[1:-1], s[2:]):
        if a * c != b * b:
            return False
    return True


def foo():
    for a in range(1, 300):
        for i in range(a + 2, a * a):
            if i % a != 0:
                s = steps(a, i)
                if len(s) > 5 and not actually_geo(s):
                    print(len(s), s)
