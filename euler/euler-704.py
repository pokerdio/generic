def twos_fact_naive(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    ret = 0
    while f % 2 == 0:
        f //= 2
        ret += 1
    return ret


def twos_fact(n):
    ret = 0
    while n > 1:
        ret += n // 2
        n //= 2
    return ret


def twos_c(n, m):
    return twos_fact(n) - twos_fact(m) - twos_fact(n - m)


def best(n):
    max = 0
    maxi = 0
    s = ""
    for i in range(1, n // 2 + 1):
        twos = twos_c(n, i)
        s = s + str(twos) + " "
        if twos > max:
            max = twos
            maxi = i
    return maxi, max, s


def pbest(n):
    for i in range(1, n + 1):
        print(best(i))
    return(sum(best(i)[1] for i in range(1, n + 1)))


def test_twos_fact():
    for i in range(1, 1000):
        assert twos_fact_naive(i) == twos_fact(i)


def foo(n, p):
    nrest = 0
    if n > 2 ** p:
        nrest = n - 2 ** p
        n = 2 ** p
    ret = (n - 1) * p
    n -= 1
    while n > 1:
        ret -= n // 2
        n //= 2
    return ret, nrest


def bar(n):
    p = 1
    ret = 0
    while True:
        delta, n = foo(n, p)
        ret += delta
        p += 1
        if not n:
            break
    return ret


def bar_test():
    for i in range(1, 100):
        assert bar(i) == pbest(i), "error on %d" % i


print(bar(10**16))
