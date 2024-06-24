

def pan_low(n):
    s = "".join(sorted(str(n)[-9:]))

    return s == "123456789"


def pan_high(n):
    s = "".join(sorted(str(n)[:9]))

    return s == "123456789"


def go(n):
    a, b = 1, 1

    c, d = 1.0, 1.0

    for i in range(3, n):
        a, b = (a + b) % 1000000000, a
        c, d = c + d, c

        if c > 1000000000:
            c /= 10.0
            d /= 10.0

        if pan_high(c) and pan_low(a):
            print("high", i, c)
            print("low", i, a)
    return c
