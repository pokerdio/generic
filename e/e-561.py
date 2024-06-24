from math import gcd

from functools import reduce


def _foo(n, m):
    p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    n = reduce(lambda x, y: x * y, p[:m]) ** n

    ret = 0
    for j in range(2, n + 1):
        if n % j == 0:
            for i in range(1, j):
                if j % i == 0:
                    ret += 1
    return ret


def foo(n=10**12, m=904961):
    inclusive_pairs = (n + 1)*(n+2) // 2
    exclusive_pairs = n*(n + 1) // 2

    pairs = 0  # count of pairs of divisors of p_m^n using only _ divisors
    ones = 1  # count of divisors that use only _ primes, upt to power n
    for _ in range(m):
        ones, pairs = (ones * (n + 1)), (pairs * inclusive_pairs + ones * exclusive_pairs)
    return pairs


def twos(n):
    ret = 0
    while n % 65536 == 0:
        ret += 16
        n //= 65536
    while n % 2 == 0:
        ret += 1
        n //= 2
    return ret


def _go(n, m):
    ret = 0
    for n in range(1, n):
        ret += foo(n, m)
    return ret

# end of helper dev functions

# next up: the code that does something


# n+1 = 4k

# ones = 4 ** m * _

# inclusive_pairs = (4k) * odd // 2 = even
# exclusive_pairs == (4k) * odd // 2 = even
# both have the same content of twos: one less than n+1

# pairs always grows by(one less twos than ones) - twos in pairs is m * (twos(n+1) - 1)


# -----

# n+1 = 4k+1 <= > n = 4k

# ones is always odd

# incl and excl are even

# incl has a solo two
# for m big, pairs grows to the twos in excl and peaks there cuz its always less than m
# numbers up to 10**12 have less than 40 twos


def go(n=10**12, m=904961):
    ret = 0

    n1 = (n + 1) // 4

    while n1 > 0:
        ret += m * n1
        n1 //= 2

    n2 = n // 4
    while n2 > 0:
        ret += n2
        n2 //= 2
    return ret


assert(go(8) == 2714886)
print(go())
