from itertools import product
from math import gcd  # gcd stands for "greatest common multiple"


def lcm(*v):
    """least common multiple"""
    ret = 1
    for i in v:
        ret = ret * i // (gcd(ret, i))
    return ret

# include exclude principle
# we add the dragons that are hurt by any one of the rules (ones divisible by k,
# ones divisible by l, ones divisibile by m and ones divisible by n)

# but we counted some of those multiple times, so we remove those divisible by both k and l,
# by both  k and m, by both k and n, by both l and m, both l and n, by both m and n

# but we counted some of those multiple times so we must add back those divisible by k l and m,
# and the other combinations of three rules

# but we counted some of those multiple times so we must remove those divisible by all four rules


def go(v, dragon_count):
    n = len(v)
    gen01 = product(*((0, 1),) * n)
    next(gen01)
    damaged_dragons = 0
    for rule_combination in gen01:
        rule_count = sum(rule_combination)

        rule_dragon_count = dragon_count // lcm(*(v[i] for i in range(n) if rule_combination[i]))
        damaged_dragons -= (-1) ** rule_count * rule_dragon_count

    return damaged_dragons


*v, d = [int(input()) for _ in range(5)]

print(go(v, d))
