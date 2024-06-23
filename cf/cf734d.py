import sys

input = sys.stdin.readline


def gen_input():
    while True:
        yield [int(c) for c in input().split()]


def gen_fake():
    yield [20, 3, 2]
    yield [10, 99]
    yield [2, 4, 3]
    yield [20, 10, 40]
    yield [4, 15]
    yield [10, 80]


def gen_fake():
    yield [20, 3, 2]
    yield [10, 99]
    yield [2, 4, 3]
    yield [200, 100, 400]
    yield [4, 15]
    yield [100, 800]


def ints(g=gen_input()):
    return next(g)


desired_potions, _, _ = ints()
seconds_per_initial, mana_store = ints()

seconds_per_alt = ints()
mana_seconds = ints()
free_potions = ints()
mana_potions = ints()


def fix_potions():
    """sort by mana cost and eliminate suboptimals"""
    v = sorted(zip(mana_potions, free_potions))
    ret = [v[0]]
    for mana_cost, free in v[1:]:
        if free > ret[-1][1]:
            ret.append((mana_cost, free))
    return ret


fixed_free = fix_potions()


def best_free_potions(available_mana):
    start, stop = 0, len(fixed_free)
    best = 0
    while stop - start >= 1:
        mid = (stop + start) // 2
        cost, gain = fixed_free[mid]
        if cost > available_mana:
            stop = mid
        elif cost <= available_mana:
            best = gain
            start = mid + 1
    return best


def solve():
    seconds_per_alt.append(seconds_per_initial)
    mana_seconds.append(0)

    best = seconds_per_initial * desired_potions

    for cost, seconds_per in zip(mana_seconds, seconds_per_alt):
        if seconds_per > seconds_per_initial:
            continue
        if cost > mana_store:
            continue
        rest_mana = mana_store - cost
        free = best_free_potions(rest_mana)

        total_time_used = max(0, desired_potions - free) * seconds_per

        best = min(best, total_time_used)
    return best


print(solve())
