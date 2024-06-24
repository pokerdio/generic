from primez import rm_prime


def digit_sum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n //= 10
    return ret


def harsh_expand(x):
    """assume x is a right truncateable harshad number"""
    x10 = x * 10
    xds = digit_sum(x)

    for i in range(10):
        x2 = i + x10
        xds2 = xds + i
        if x2 % xds2 == 0:
            yield x2


def prime_expand(x):
    """assume x is a right truncateable harshad number"""
    if not rm_prime(x // digit_sum(x)):
        return

    x10 = x * 10
    for i in range(10):
        x2 = i + x10
        if rm_prime(x2):
            print("hoorah", x2)
            yield x2


def go(n):
    h = list(range(1, 10))
    s = 0
    for k in range(n):
        h2 = []
        for i in h:
            s += sum(prime_expand(i))

        if k == n - 1:
            return s

        for i in h:
            h2 += list(harsh_expand(i))

        h = h2

    assert(False)
