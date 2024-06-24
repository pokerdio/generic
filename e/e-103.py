from itertools import combinations, product


def bump(s):
    m = s[len(s) // 2]
    s = [m] + [(m + a) for a in s]
    return s


def bumpn(n):
    s = [1]
    for _ in range(n - 1):
        s = bump(s)

    return s


def special_sum(s):
    n = len(s)
    for i in range(n):
        a, b = s[:i + 1], s[n - i:]
        if sum(a) <= sum(b):
            return False

    sums = set()
    for m in range(1, n + 1):
        for sub in combinations(s, m):
            subsum = sum(sub)
            if subsum in sums:
                return False
            sums.add(subsum)

    return True


def wobble(s, delta):
    best = sum(s)
    bests = s
    for vdelta in product(range(-delta, delta + 1), repeat=len(s)):
        s2 = [a + b for a, b in zip(s, vdelta)]
        sums2 = sum(s2)
        if sums2 < best:
            if special_sum(s2):
                best = sums2
                bests = s2
    return bests


def foo():
    s6 = bumpn(6)

    s6 = wobble(s6, 1)

    s7 = bump(s6)
    print(s7)
    s7 = wobble(s7, 1)
    print(s7)
    s7 = wobble(s7, 1)
    print(s7)
    s7 = wobble(s7, 1)
    print(s7)
    s7 = wobble(s7, 2)
    print(s7)
    s7 = wobble(s7, 2)
    print(s7)
    s7 = wobble(s7, 2)
    print(s7)
    s7 = wobble(s7, 3)
    print(s7)
