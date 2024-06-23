import primez
from itertools import product
from functools import reduce


def go(n, max, level, divz):
    #    print("go", n, max, level, divz)
    if level == 1:
        if n <= max:
            yield (n, )
            return
    mini = n ** (1 / level) - 0.01
    for p in product(*(range(x + 1) for x in divz.values())):
        n2 = 1

        keyz = list(zip(divz.keys(), p))
        for i, j in keyz:
            n2 *= (i ** j)
            divz[i] -= j

        nrest = n // n2

        if n2 > mini and n2 <= max and ((level < 4) or (nrest + 2 > n2)):
            for x in go(nrest, n2, level - 1, divz):
                yield (n2, *x)

        for i, j in keyz:
            divz[i] += j


def solve(n):
    s = 0
    divz = {i: 2 * j for i, j in primez.decompose(n).items()}
#    print(divz)
    for sa, sb, sc, sd in go(n**2, n**2, 4, divz):
        abcd = sa + sb + sc + sd
        if abcd % 2 != 0:
            continue
        abcd //= 2
        a, b, c, d = abcd - sa, abcd - sb, abcd - sc, abcd - sd

#        print("testing", a, b, c, d, "|", sa, sb, sc, sd, "|", abcd)
        if min(a, b, c, d) <= 0:
            continue
        if a + b + c <= d:
            continue
#        print("success", a, b, c, d)
        s += a + b + c + d
    return s


def main(n):
    s = 0
    for i in range(n, 0, -1):
        if i % 100 == 0:
            print(i, s)
        s += solve(i)
    return s

# print(main(1000000))
# 2611227421428
