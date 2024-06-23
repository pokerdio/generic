import numpy as np


# fuck you solution based on iterative optimization, pushing the precision
# until the result stopped changing

def alter(v, pos, alter_factor):
    v = v.copy()

    v[pos] *= alter_factor
    v /= (sum(v) / len(v))
    return v


def value(v):
    ret = 1.0
    for i in range(len(v)):
        ret *= v[i] ** (i + 1)
    return ret


def initv(n):
    v = np.array([1.0] * n)
    return v


def optimize(v, alter_factor):
    value0 = value(v)
    bestvalue = value0
    bestv = v
    for i in range(len(v)):
        v1 = alter(v, i, alter_factor)
        value1 = value(v1)
        if value1 > bestvalue:
            bestvalue = value1
            bestv = v1
    return value0 < bestvalue, bestvalue, bestv


def go(n):
    v = initv(n)

    for i in range(16):
        alter_factor = 1.0 + (0.4 ** i)
        for _ in range(1000):
            changed, best, v = optimize(v, alter_factor)
            if not changed:
                break

    return best, v


#print(sum(int(go(n)[0]) for n in range(2, 16)))

# after looking at the results, you can just guess the correct formula

def go2(n):
    v = np.array([i + 1.0 for i in range(n)])
    v /= (sum(v) / n)
    return value(v), v


print(sum(int(go2(n)[0]) for n in range(2, 16)))
