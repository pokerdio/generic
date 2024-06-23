def red(n):
    a = 1
    b = 2
    while n > 2:
        n -= 1
        b, a = a + b, b

    return b - 1


def green(n):
    a, b, c = 1, 1, 2

    while n > 3:
        n -= 1
        c, b, a = a + c, c, b

    return c - 1


def blue(n):
    a, b, c, d = 1, 1, 1, 2

    while n > 4:
        n -= 1
        d, c, b, a = a + d,  d, c, b,

    return d - 1


def rgb(n):
    a, b, c, d = 1, 1, 2, 4,

    while n > 3:
        n -= 1
        d, c, b, a = a + b + c + d,  d, c, b,

    return d


def foo(n):
    return red(n) + green(n) + blue(n)


print("problem 116", foo(50))
print("problem 117", rgb(50))
