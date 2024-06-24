def F(n, a=None, b=None, c=None, v=[1]):
    #    print(f"enter F({n})")
    if a:
        v[0] = (a, b, c)
    else:
        a, b, c = v[0]
    if n > b:
        ret = n-c
    else:
        ret = F(a + F(a + F(a + F(a + n))))
#    print(f"exit F({n}) = {ret}")
    return ret


def f(n):
    return F(n, 50, 2000, 40)


def foo(start=1951):
    s = 0
    for i in range(start, 2001):
        s += f(i)
    return s


def bar(a, b, c):
    k = b

    s = 0

    f = F(b, a, b, c)

    xxx = 0
    while k >= a:
        s += (f + f - a + 1) * a // 2

        xxx += 1
        if xxx % 100000 == 0:
            print(k)
        k -= a
        f += 3 * (a - c)

    s += (f + f - k) * (k + 1) // 2

    return s


print(bar(21**7, 7**21, 12**7))
