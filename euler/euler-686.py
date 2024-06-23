def foo_cycle(ndigitz):
    ten = 10 ** ndigitz
    v = [1]
    s = set(v)

    k = 1
    while True:
        k *= 2
        if k >= ten:
            k //= 10

        v.append(k)
        if k in s:
            return v
        s.add(k)


def foo_first(n, ten):
    while n > ten:
        n //= 10
    return n


def foo_count(cycle, value, count):
    ten = 1
    while ten < value:
        ten *= 10

    cyclestart = cycle.index(cycle[-1]) + 1

    for i in range(cyclestart):
        if foo_first(cycle[i], ten) == value:
            count -= 1
            if count == 0:
                return i

    cycle_count = 0
    for i in range(cyclestart, len(cycle)):
        if foo_first(cycle[i], ten) == value:
            cycle_count += 1

    complete_cycles = count // cycle_count
    count %= cycle_count

    if count == 0:
        return len(cycle)

    for i in range(cyclestart, len(cycle)):
        if foo_first(cycle[i], ten) == value:
            count -= 1
            if count == 0:
                return i + complete_cycles * (len(cycle) - cyclestart) - 1
    assert(False)
