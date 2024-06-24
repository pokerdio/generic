

words = ["free", "fare", "area", "reef"]


def expand(state):
    global words
    for c in "aefr":
        v = list(state)
        for w in range(4):
            word = words[w]
            if c == word[state[w] % 4]:
                v[w] += 1
                if v[w] == 4 and word[0] == c:  # hack to exclude AREAREA
                    v[w] = 5
            else:
                v[w] = (v[w] // 4) * 4
                # bullshit hack to exclude FRFREE
                if c == word[0]:
                    v[w] += 1

        if 8 not in v:
            yield tuple(v)


def step(v):
    v2 = {}
    for state, count in v.items():
        for newstate in expand(state):
            v2[newstate] = v2.get(newstate, 0) + count
    return v2


def go(n):
    v = {(0, 0, 0, 0): 1}
    for i in range(n):
        v = step(v)

    return sum((count for state, count in v.items() if min(state) >= 4))
