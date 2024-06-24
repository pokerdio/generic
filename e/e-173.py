#!/usr/bin/env python3



def solve(n):
    n = n // 4
    s = 0
    for i in range(2, n + 1):
        #print(i, min(i - 1, n // i))
        s += min(i - 1, n // i)
    return s


print(solve(1000000))
