def gen_single_layer(n):
    if n == 4:
        yield (2,)
        return
    if n == 3 or n == 2:
        yield tuple()
        return

    if n < 2:
        return

    for delta in range(2, 4):
        for lay in gen_single_layer(n - delta):
            yield (delta,) + tuple(delta + x for x in lay)


def go(w, h):
    base = list(gen_single_layer(w))

    base_set = {x: set(x) for x in base}
    base_compat = {x: [b for b in base if not base_set[b] & base_set[x]]
                   for x in base}

    v = {b: 1 for b in base}

    for _ in range(h - 1):
        v2 = {}
        for b, count in v.items():
            for compat in base_compat[b]:
                v2[compat] = v2.get(compat, 0) + count
        v = v2

    return sum(list(v2.values()))
