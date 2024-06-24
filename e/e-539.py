def p_rec(n):
    if n <= 2:
        return n
    return (2 * (n // 2 + 1 - p_rec(n // 2))) % 987654321


def s_rec(n):
    if n == 1:
        return 1
    r = 0
    if n % 2:
        r = p_rec(n)
        n -= 1
    n2 = n // 2
    return (r + 2 * n2 * (n2 + 3) - 4 * s_rec(n2) - p_rec(n + 1) + 1) % 987654321


print(s_rec(10**18))
