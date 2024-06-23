from collections import Counter as C
t = int(input())


def go(n, m):
    ret = 0
    while n > m:
        ret += 1   # duplication
        swaps = min(m, n - m)
        ret += swaps
        m += swaps
    return ret


for _ in range(t):
    n = int(input())
    v = [int(c) for c in input().split()]
    m = max(C(v).values())
    print(go(n, m))
