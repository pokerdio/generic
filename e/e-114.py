

def memoize2(f):
    memo = {}

    def helper(n, k):
        if (n, k) not in memo:
            memo[(n, k)] = f(n, k)
        return memo[(n, k)]

    return helper


@memoize2
def break_n(n, k):
    if k == 1:
        return 1

    if k == 2:
        return n + 1

    if n == 0:
        return 1

    if n == 1:
        return k

    return sum(break_n(n - c, k - 1) for c in range(n + 1))


def count_combos(n, m):
    red_blocks = 0

    s = 0
    while red_blocks * m + red_blocks - 1 <= n:
        s += break_n(n - (red_blocks * m + red_blocks - 1), red_blocks * 2 + 1)
        red_blocks += 1

    return s


# this solves problem 115:
def more_than_combos(n, m):
    for i in range(10**6):
        if count_combos(i, m) >= n:
            return i
