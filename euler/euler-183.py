import fractions as F


def f(n, k):
    return log(n / k) * k


def optimize(n, k0):
    v = f(n, k0)
    k = k0

    bumped = False
    bestk = k0

    while True:
        k += 1
        v2 = f(n, k)
        if v2 >= v:
            v = v2
            bumped = True
            bestk = k
        else:
            break

    if bumped:
        return bestk

    while k > 1:
        k -= 1
        v2 = f(n, k)
        if v2 >= v:
            v = v2
            bumped = True
            bestk = k
        else:
            break
    return bestk


def terminating(n, k):
    f = F.Fraction(n, k)
    d = f.denominator
    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5
    return d > 1


def go(n):
    k = 2
    s = 0
    for i in range(5, n + 1):
        k = optimize(i, k)
        if terminating(i, k):
            s += i
        else:
            s -= i

    return s
