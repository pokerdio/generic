#!/usr/bin/env python3

# of all the proper divisors of the sum of their own sum of proper
# divisors)

# e.g. 284 and 220 are reciprocally equal to the others sum of proper divisors
# 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284;


def DivisorsSum(n):
    divisors_sum = {1: 0}
    for i in range(1, n // 2 + 1):
        for j in range(i * 2, n, i):
            divisors_sum[j] = divisors_sum.get(j, 0) + i

    return divisors_sum


def AmicablesSum(n):
    d = DivisorsSum(n)
    d = DivisorsSum(max(d.values()) + 1)

    sum = 0
    for i in range(2, n):
        if d[i] != i and d[d[i]] == i:
            sum += i

    return(sum)


print(AmicablesSum(10000))
