from primez import totient as toti
import primez


def foo(n):
    t0 = toti(n)

    for i in range(2, 7):
        totini = toti(n ** i)
        print(totini, t0 * (n ** (i - 1)), gcd(t0, n + 1))


# s = t0 + t0 * n + t0 * n * n + ... + t0 * n ** (n-1)
# sn = t0 * n + ... + t0 * n ** n
# s(n-1) = t0(n**n - 1)


def above(low, p):
    x = low % p
    return p - x if x else 0


def interval_divz(low, high):
    a = [None] * (high - low)
    ln = len(a)
    for p in primez.iterate_primez(int(sqrt(high)) + 2):
        start = above(low, p)
        for i in range(start, ln, p):
            if not a[i]:
                a[i] = [p]
            else:
                a[i].append(p)
    return a
