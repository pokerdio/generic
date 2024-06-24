#!/usr/bin/env python3

# https://projecteuler.net/problem=46 goldbach false conjecture: every
# odd composite number can be written as the sum of a prime and twice
# a square


def go(n=9999):
    primez = [2, 3, 5, 7]

    for i in range(9, n, 2):
        notprime = False
        for prime in primez:
            if i % prime == 0:
                notprime = True
                break
        if notprime:
            ok = False
            for prime in primez[1:]:
                squared = (i - prime) // 2
                root = int(squared ** 0.5)
                if root * root == squared:
                    ok = True
                    break
            if not ok:
                print("fail at ", i)
                return
        else:
            primez.append(i)


go()
