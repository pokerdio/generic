#!/usr/bin/env python3



def step(n):
    return sum(int(c)**2 for c in str(n))


def one_or_eightynine(n):
    while n != 1 and n != 89:
        n = step(n)
    return n


print(sum(one_or_eightynine(n) == 89 for n in range(2, 10**7 + 1)))
