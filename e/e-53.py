def go(n):
    s = 0

    x = n
    for i in range(2, n):
        x *= (n - i + 1)
        x //= (i)
        s += (x > 1000000)
    return s


def solve(n):
    return sum((go(i) for i in range(3, n + 1)))
