def foo(n):
    s = 0
    while True:
        while n % 7 == 0:
            n //= 7

        if n == 1:
            return s

        s += 7 - (n % 7)
        n = (n // 7) * 7 + 7


def octo(n):
    s = ""
    while n > 0:
        s = str(n % 7) + s
        n //= 7
    return s


def dec(s):
    n = 0
    for i in (int(c) for c in s):
        n *= 7
        n += i
        print(n)
    return n


def h(n):
    sevenn = 7 ** n
    x = (sevenn - 1) // 11
    if x * 11 + 1 == sevenn:
        return x
