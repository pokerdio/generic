import primez
import itertools


# numbering the cards 0 to n-1, n even, the transformation goes
# x->(2x%(n-1))
# so the card 1 must return to  1 after 60 steps
# so 2**60%(n-1) must = 1


#2**60 - 1 == x * (n - 1)


def shuffle(x):
    return (*x[0::2], *x[1::2])


def step(x, n):
    if x < n // 2:
        return x * 2
    else:
        return (x - n // 2) * 2 + 1


def step2(x, n):
    return (x * 2) % (n - 1)


def teststep(n):
    for i in range(1, n):
        if step(i, n) != step2(i, n):
            print("error", i, step(i, n), step2(i, n))


def onepath(n, max=100):
    s = ""
    x = 1
    k = 0
    for _ in range(max):
        x = step(x, n)
        k += 1
        if x == 1:
            return k


def test_cycle(n, max_cycle=1000):
    v = tuple(range(n))
    v2 = v
    for k in range(1, max_cycle + 1):
        v2 = shuffle(v2)
        if v2 == v:
            return k


def foo2(n=60):
    for i in range(2, 1000, 2):
        v = tuple(range(i))
        v2 = v
        for k in range(1, n + 1):
            v2 = shuffle(v2)
            if v2 == v:
                if k == n:
                    print(i, k, "{0:b}".format(i))
                break


def foo3(n):
    v = [1] * n


def decompose(n, maxp=1000000):
    g = {}
    for i in primez.iterate_primez(maxp):
        while n % i == 0:
            n //= i
            g[i] = g.get(i, 0) + 1
    return g, n


def divz(g):
    g = sorted(list(g.items()))
    p = [[x[0] ** y for y in range(x[1] + 1)] for x in g]

    for c in itertools.product(*p):
        n = 1
        for x in c:
            n *= x

        if onepath(n + 1, 60) == 60:
            yield n + 1


print(sum(divz(decompose(2**60 - 1)[0])))
