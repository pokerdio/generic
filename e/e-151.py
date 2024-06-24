from fractions import Fraction as F


def expand(v):
    """how many a1, a2,..., a5 pages"""
    for i in range(1, 6):
        if v[i]:
            v2 = *v[1:i], v[i] - 1, *(x + 1 for x in v[i + 1:])

            yield (v[0] + (sum(v2) == 1), *v2), v[i]


def go(n=14):
    v = {(0, 1, 0, 0, 0, 0): 1}

    for i in range(n):
        v2 = {}

        for poz, count in v.items():
            s = sum(poz[1:])
            for poz2, multiplier in expand(poz):
                v2[poz2] = v2.get(poz2, 0) + count * multiplier / s

        v = v2

    total_solo, total = 0, 0
    for poz, count in v.items():
        total_solo += poz[0] * count
        total += count
    return "%.6f" % (total_solo / total)


# def randchoose(v):
#     s = randint(sum(v))
#     for i in range(len(v)):
#         s -= v[i]
#         if s < 0:
#             return i


# def mc(n=14, verbose=False):
#     v = (1, 0, 0, 0, 0)
#     s = 0
#     for i in range(n):
#         k = randchoose(v)
#         v = (*v[:k], v[k] - 1, *(x + 1 for x in v[k + 1:]))
#         if sum(v) == 1:
#             s += 1
#         if verbose:
#             print(v, s)

#     return (s, *v)


# def makedict(f, runs, *arg):
#     v = {}

#     for _ in range(runs):
#         val = f(*arg)
#         v[val] = v.get(val, 0) + 1
#     return v


print(go())
