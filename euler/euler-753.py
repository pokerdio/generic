

def foo(n):
    return set(x * x * x % n for x in range(1, n))


def bar(gen):
    y = next(gen)
    for x in gen:
        yield x - y
        y = x


def foo2(n):
    return list(x ** 3 % n for x in range(1, n))


def foo3(n):
    g = {}
    for i in range(1, n):
        j = i ** 3 % n

        g[j] = g.get(j, 0) + 1
    return g
