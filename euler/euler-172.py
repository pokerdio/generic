def expand(poz):
    threes, twos, ones, zeros = poz

    s = 0
    if threes:
        yield (threes - 1, twos + 1, ones, zeros), threes
    if twos:
        yield (threes, twos - 1, ones + 1, zeros), twos
    if ones:
        yield (threes, twos, ones - 1, zeros + 1), ones


def go(digitz):
    assert(digitz > 1)

    v = {(9, 1, 0, 0): 9}  # 9 options for the first digit (0 excluded)

    for _ in range(digitz - 1):
        v2 = {}
        for poz, count in v.items():
            for poz2, count2 in expand(poz):
                v2[poz2] = v2.get(poz2, 0) + count * count2

        v = v2
    return sum(list(v.values()))


print(go(18))
