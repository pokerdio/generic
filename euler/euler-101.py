import numpy as np


def foo(n):
    minus = 1
    s = 0
    for i in range(11):
        s += minus * (n ** i)
        minus = -minus
    return s


def solve(n, foo=foo):
    b = np.array(list(foo(x) for x in range(1, n + 1)))

    A = np.array([[x ** i for i in range(n)] for x in range(1, n + 1)])
    return np.linalg.solve(A, b)


def go(n, foo=foo):
    ret = 0
    for x in range(1, n + 1):
        v = solve(x, foo)
        s = sum(v[i] * ((x + 1) ** i) for i in range(x))
        ret += s
    return ret


print(go(10))
