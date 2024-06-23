from builtins import sum


def unpair(v):
    n = max(max(pair) for pair in v)
    mate = list(range(n))
    for a, b in v:
        mate[a - 1] = b - 1
        mate[b - 1] = a - 1
    return mate


def load():
    bed_pairs = []
    with open("p673_beds.txt", "r") as f:
        for s in f.readlines():
            bed_pairs.append(tuple(int(x) for x in s.strip().split(",")))
    desk_pairs = []
    with open("p673_desks.txt", "r") as f:
        for s in f.readlines():
            desk_pairs.append(tuple(int(x) for x in s.strip().split(",")))

    return unpair(bed_pairs), unpair(desk_pairs)


beds, desks = load()
ok = [True] * len(beds)
n = len(beds)


def count_loners():
    ret = 0
    for i in range(n):
        if beds[i] == i and desks[i] == i:
            ok[i] = False
            ret += 1

    return ret


def trace_cycle(i):
    assert desks[i] != i and beds[i] != i
    initial_i = i
    last = i
    ok[i] = False
    i = beds[i]
    cy_length = 1
    while initial_i != i:
        cy_length += 1
        assert ok[i]
        ok[i] = False

        if beds[i] == last:
            last = i
            i = desks[i]
        elif desks[i] == last:
            last = i
            i = beds[i]
    return cy_length


def trace_chain(i):
    """i has to be a chain start, either a solo bed or desk"""
    assert (desks[i] == i or beds[i] == i)
    ok[i] = False
    last = i
    length = 1
    while True:
        if beds[i] == last:  # if beds are forbidden, try the desk route
            if desks[i] == i:  # end of the line
                return length, "desk"
            last = i
            i = desks[i]
        elif desks[i] == last:  # if desks are forbidden try the desk route
            if beds[i] == i:
                return length, "bed"
            last = i
            i = beds[i]
        length += 1
        ok[i] = False


def count_chains():
    """counts chains starting in a bed"""
    bb = {}  # chains starting in a lonely bed endingin a lonely bed, by chain length
    bd = {}  # chains starting in a lonely bed ending in a loenly desk
    dd = {}  # chains starting in a lonely desk ending in a loenly desk
    # chains starting in a lonely desk ending in a lonely bed are stored in bd too!
    for i in range(n):
        if ok[i]:
            if beds[i] == i and desks[i] != i:  # lonely bed, paired desk
                last_ok = sum(ok)
                chain_length, chain_outro = trace_chain(i)
                assert last_ok - chain_length == sum(ok)
                if chain_outro == "bed":
                    bb[chain_length] = bb.get(chain_length, 0) + 1
                elif chain_outro == "desk":
                    bd[chain_length] = bd.get(chain_length, 0) + 1
                else:
                    assert False
            if desks[i] == i and beds[i] != i:
                last_ok = sum(ok)
                chain_length, chain_outro = trace_chain(i)
                assert last_ok - chain_length == sum(ok)
                if chain_outro == "bed":
                    bd[chain_length] = bd.get(chain_length, 0) + 1
                elif chain_outro == "desk":
                    dd[chain_length] = dd.get(chain_length, 0) + 1
                else:
                    assert False
    return bb, bd, dd


def count_cycles():
    cy = {}
    for i in range(n):
        if ok[i]:
            assert desks[i] != i and beds[i] != i  # all chains/loners must be gone already
            last_ok = sum(ok)
            cycle_length = trace_cycle(i)
            print(i, last_ok, cycle_length, sum(ok))
            assert sum(ok) == last_ok - cycle_length
            cy[cycle_length] = cy.get(cycle_length, 0) + 1
    return cy


def total(d):
    return sum(len * count for len, count in d.items())


def fact(n, mod):
    ret = 1
    for i in range(2, n + 1):
        ret = i * ret % mod
    return ret


def go(mod=999999937):
    solo = count_loners()
    a, b, c = count_chains()
    cy = count_cycles()

    ret = fact(solo, mod)   # loners are just permutated
    for len, count in a.items():
        ret = ret * fact(count, mod) % mod
        ret = ret * (2 ** count) % mod  # mapping between two bb/dd chains can be done in two ways

    for len, count in c.items():
        ret = ret * fact(count, mod) % mod
        ret = ret * (2 ** count) % mod
    for len, count in b.items():
        ret = ret * fact(count, mod) % mod
    for len, count in cy.items():
        ret = ret * fact(count, mod) % mod
        ret = ret * (len ** count) % mod
    return ret
