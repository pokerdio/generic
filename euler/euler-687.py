from fractions import Fraction as Fr


def ncards(upcard, four, three, live2, dead2, live1, dead1, live0, dead0):
    return four * 4 + three * 3 + (live2 + dead2) * 2 + live1 + dead1


def expandexcept(s, cards, ex=None):
    """state expansions that are unrelated to the upcard"""
    upcard, four, three, live2, dead2, live1, dead1, live0, dead0 = s

    if four > 0:
        yield("three", four - 1, three + 1, live2, dead2, live1, dead1, live0, dead0), \
            4 * four / cards

    if ex != "three" and three > 0:
        yield("live2", four, three - 1, live2 + 1, dead2, live1, dead1, live0, dead0), \
            3 * three / cards

    if ex != "live2" and live2 > 0:
        yield("live1", four, three, live2 - 1, dead2, live1 + 1, dead1, live0, dead0), \
            live2 * 2 / cards

    if ex != "live1" and live1 > 0:
        yield("zero", four, three, live2, dead2, live1 - 1, dead1, live0 + 1, dead0), \
            live1 / cards

    if dead2 > 0:
        yield("dead1", four, three, live2, dead2 - 1, live1, dead1 + 1, live0, dead0), \
            dead2 * 2 / cards
    if dead1 > 0:
        yield("zero", four, three, live2, dead2, live1, dead1 - 1, live0, dead0 + 1), \
            dead1 / cards


def expand(s):
    upcard, four, three, live2, dead2, live1, dead1, live0, dead0 = s

    cards = Fr(four * 4 + three * 3 + (live2 + dead2) * 2 + live1 + dead1)

    if not cards:
        return

    if upcard == "three":
        assert(three > 0)
        yield ("dead2", four, three - 1, live2, dead2 + 1, live1, dead1, live0, dead0), \
            3 / cards
        if three > 1:
            yield("live2", four, three - 1, live2 + 1, dead2, live1, dead1, live0, dead0), \
                3 * (three - 1) / cards
        yield from expandexcept(s, cards, "three")
    elif upcard == "live2":
        assert(live2 > 0)
        yield ("dead1", four, three, live2 - 1, dead2, live1, dead1 + 1, live0, dead0), \
            2 / cards
        if live2 > 1:
            yield("live1", four, three, live2 - 1, dead2, live1 + 1, dead1, live0, dead0), \
                (live2 - 1) * 2 / cards
        yield from expandexcept(s, cards, "live2")
    elif upcard == "live1":
        assert(live1 > 0)
        yield ("zero", four, three, live2, dead2, live1 - 1, dead1, live0, dead0 + 1), \
            1 / cards
        if live1 > 1:
            yield("zero", four, three, live2, dead2, live1 - 1, dead1, live0 + 1, dead0), \
                (live1 - 1) / cards
        yield from expandexcept(s, cards, "live1")
    elif upcard == "dead2":
        assert(dead2 > 0)
        yield from expandexcept(s, cards)
    elif upcard == "dead1":
        assert(dead1 > 0)
        yield from expandexcept(s, cards)
    elif upcard == "zero":
        yield from expandexcept(s, cards)


def step(v):
    v2 = {}
    for st, prob in v.items():
        for next_st, p2 in expand(st):
            v2[next_st] = v2.get(next_st, 0) + prob * p2
    return v2


def prime_perfect_rank_prob(v):
    prime = {2, 3, 5, 7, 11, 13}
    ret = 0
    for st, p in v.items():
        if st[-2] in prime:
            ret += p
    return float(ret)


def total_prob(v):
    ret = 0
    for st, p in v.items():
        ret += p
    return float(ret)


def ev_perfect(v):
    ret = 0
    for st, p in v.items():
        ret += p * st[-2]

    return ret, float(ret)


def print_final(v):
    for st, p in v.items():
        if st[-1] + st[-2] == 13:
            print("%d - %.4f" % (st[-2], p))


def go():
    v = {("zero", 13, 0, 0, 0, 0, 0, 0, 0): Fr(1)}
    for i in range(52):
        v = step(v)
    print("%.10f" % prime_perfect_rank_prob(v))


# 0.3285320869
