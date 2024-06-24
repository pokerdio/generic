import sympy


def go(col, ncol, constraints):
    if not constraints:
        return 1
    forbidden = set(col[i] for i in constraints[0])

    ret = 0

    rest_constraints = constraints[1:]
    for c in set(col):
        if c not in forbidden:
            ret += go(col + (c,), ncol, rest_constraints)
    if ncol > 0:
        ret += ncol * go((*col, max(col) + 1), ncol - 1, rest_constraints)

    return ret


def amulti(ncol):
    return go((0, 1), ncol - 2, ((1,), (1, 2), (3,), (0, 4), (0, 2, 5)))


def bmulti(ncol):
    return go((0, 1), ncol - 2, ((1,), (1, 2), (3,), (0, 4), (2, 5)))


def btest():
    return 4 * 3 * (bmed(4) ** 2)


assert(btest() == 92928)


def solve(a, b, ncol):
    am, bm = amulti(ncol), bmulti(ncol)
    return (am ** a) * (bm ** b) * sympy.binomial(a + b, a) * ncol * (ncol - 1)


print(str(solve(25, 75, 1984))[-8:])
