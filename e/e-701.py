def mk_subsets(n):
    for i in range(2**n):
        yield tuple(i & (2 ** j) and 1 or 0 for j in range(n))


def convert_subset(sub):
    i = 0
    n = len(sub)
    ret = []
    while i < n:
        while i < n and not sub[i]:
            i += 1
        start = i
        while i < n and sub[i]:
            i += 1
        if start < i:
            ret.append((start, i))
    return ret


def mk_state(subset):
    """a state is the biggest dead area followed by a list of:
    surface id (0 none) followed by a list of total areas by id"""
    active_shooter = False
    id = []
    area = []
    for i in range(len(subset)):
        col = subset[i]
        if col:
            if active_shooter:
                area[-1] += 1
            else:
                area.append(1)
                active_shooter = True
            id.append(len(area) - 1)
        else:
            active_shooter = 0
            id.append(-1)
    return (0, tuple(id), tuple(area))


def grow(state, subset):
    """subset must be in interval list format"""
    cut_off, id, area = state
    id = list(id)

    for start, stop in subset:
        first = None
        for i in range(start, stop):
            if id[i] >= 0:
                if first and idd[i] != first:
                    merge.add(id[i])
                if not first:
                    first = id[i]


def go(n):
    ss = list(mk_subsets(n))
