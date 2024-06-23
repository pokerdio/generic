def ints():
    return [int(x) for x in input().split()]


def foo(n, k, t):
    a = t*n*k // 100
    return " ".join(str(x) for x in [k] * (a // k) + [a % k] * (t < 100) + [0] * (n - (a//k) - 1))


print(foo(*ints()))
