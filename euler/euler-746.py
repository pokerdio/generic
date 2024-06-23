import primez


def pp(state):
    n, sm, sw, bsm, bsw, fam, f1 = state
    print("unseated total %d - solved m %d w %d - buf m %d w %d - unseated fams %d fam1 %d" %
          (n, sm, sw, sm, sw, fam, f1))


def expand(state):
    n, sm, sw, bsm, bsw, fam, f1 = state
    if n % 2:  # man needs to be seated
        if f1 == 1 and n > f1:  # m
            yield ((n - 1, sm + bsm, sw + bsw, 0, 0, fam, 0), 1)
        if f1 == 2 and n > f1:  # wm
            yield ((n - 1, sm + bsm, sw + bsw + 1, 0, 0, fam, 0), 1)
        if f1 == 3 and n > f1:  # mwm in play in the one family
            yield ((n - 1, sm + bsm + 1, sw + bsw + 1, 0, 0, fam, 0), 2)
        if sm:
            yield ((n - 1, sm + bsm - 1, sw + bsw, 0, 0, fam, abs(f1)), sm)
        if fam:  # and n > 4:
            yield ((n - 1, sm + bsm, sw + bsw, 1, 2, fam - 1, abs(f1)), fam * 2)
            yield ((n - 2, sm + bsm, sw + bsw, 1, 1, fam - 1, abs(f1)), fam * 4)
            yield ((n - 3, sm + bsm, sw + bsw, 0, 1, fam - 1, abs(f1)), fam * 4)
    else:  # woman needs to be seated
        if f1 == 2 and n > f1:  # wm
            yield ((n - 1, sm + bsm + 1, sw + bsw, 0, 0, fam, 0), 1)
        if f1 == 3 and n > f1:  # mwm
            yield ((n - 1, sm + bsm + 2, sw + bsw, 0, 0, fam, 0), 1)
        if sw:
            yield ((n - 1, sm + bsm, sw + bsw - 1, 0, 0, fam, abs(f1)), sw)
        if fam:  # and n > 4:
            yield ((n - 1, sm + bsm, sw + bsw, 2, 1, fam - 1, abs(f1)), fam * 2)
            yield ((n - 2, sm + bsm, sw + bsw, 1, 1, fam - 1, abs(f1)), fam * 4)
            yield ((n - 3, sm + bsm, sw + bsw, 1, 0, fam - 1, abs(f1)), fam * 4)


def go(n):
    print("go", n)
    s0 = (n * 4 - 1, 0, 0, 0, 0, n - 1, -3)
    s1 = (n * 4 - 2, 0, 0, 0, 0, n - 1, -2)
    s2 = (n * 4 - 3, 0, 0, 0, 0, n - 1, -1)

    v = [{s0: 1}, {s1: 2}, {s2: 2}, {}]

    for i in range(n * 4 - 1, 0, -1):
        for state, multi in v[0].items():
            for newstate, newmulti in expand(state):
                d = v[i - newstate[0]]
                d[newstate] = (d.get(newstate, 0) + multi * newmulti) % 1000000007
        v = v[1:] + [{}]
    return (v[0][(0, 0, 0, 0, 0, 0, 0)] * n * 4) % 1000000007


def S(n):
    return sum(go(i) for i in range(2, n + 1)) % 1000000007
# 582994639


def expand2(state):
    n, sm, sw, bsm, bsw, fam, f1 = state

    f2 = abs(f1) - (f1 == 4) * 4

    if n % 2:  # man needs to be seated
        if f1 == 1:  # m
            yield ((n - 1, sm + bsm, sw + bsw, 0, 0, fam, (n % 4 == 1) and 4), 1)
        if f1 == 2:  # wm
            yield ((n - 1, sm + bsm, sw + bsw, 0, 1, fam, 0), 1)
            yield ((n - 2, sm + bsm, sw + bsw, 0, 0, fam, (n % 4 == 2) and 4), 1)
        if f1 == 3:  # mwm in play in the one family
            yield ((n - 1, sm + bsm, sw + bsw, 1, 1, fam, 0), 2)
            yield ((n - 2, sm + bsm, sw + bsw, 1, 0, fam, 0), 2)
            yield ((n - 3, sm + bsm, sw + bsw, 0, 0, fam, (n % 4 == 3) and 4), 2)
        if sm:
            yield ((n - 1, sm + bsm - 1, sw + bsw, 0, 0, fam, f2), sm)
        if fam:
            yield ((n - 1, sm + bsm, sw + bsw, 1, 2, fam - 1, f2), fam * 2)
            yield ((n - 2, sm + bsm, sw + bsw, 1, 1, fam - 1, f2), fam * 4)
            yield ((n - 3, sm + bsm, sw + bsw, 0, 1, fam - 1, f2), fam * 4)
    else:  # woman needs to be seated
        if f1 == 2:  # wm
            yield ((n - 1, sm + bsm, sw + bsw, 1, 0, fam, 0), 1)
            yield ((n - 2, sm + bsm, sw + bsw, 0, 0, fam, (n % 4 == 2) and 4), 1)
        if f1 == 3:  # mwm
            yield ((n - 1, sm + bsm + 2, sw + bsw, 0, 0, fam, 0), 1)

        if sw:
            yield ((n - 1, sm + bsm, sw + bsw - 1, 0, 0, fam, f2), sw)
        if fam:
            yield ((n - 1, sm + bsm, sw + bsw, 2, 1, fam - 1, f2), fam * 2)
            yield ((n - 2, sm + bsm, sw + bsw, 1, 1, fam - 1, f2), fam * 4)
            yield ((n - 3, sm + bsm, sw + bsw, 1, 0, fam - 1, f2), fam * 4)


def rescue(x, m, n):
    c = 1

    for i in range(m + 1, n + 1):
        c *= i
    for i in range(1, n - m + 1):
        c //= i

    print("c", m, n, c)

    return (x * primez.rev(c, 1000000007)) % 1000000007


def go2(n):
    print("go", n)
    s0 = (n * 4 - 1, 0, 0, 0, 0, n - 1, -3)
    s1 = (n * 4 - 2, 0, 0, 0, 0, n - 1, -2)
    s2 = (n * 4 - 3, 0, 0, 0, 0, n - 1, -1)

    v = [{s0: 1}, {s1: 2}, {s2: 2}, {}]

    rescue_sum = 0
    for i in range(n * 4 - 1, 0, -1):
        if i % 4 == 0:
            rescue_sum += rescue(v[0].get((i, 0, 0, 0, 0, i // 4, 0), 0) *
                                 (n * 4 - i), n - i // 4 - 1, n - 1)
        for state, multi in v[0].items():
            for newstate, newmulti in expand2(state):
                d = v[i - newstate[0]]
                d[newstate] = (d.get(newstate, 0) + multi * newmulti) % 1000000007
        v = v[1:] + [{}]
    return (rescue_sum + v[0][(0, 0, 0, 0, 0, 0, 0)] * n * 4) % 1000000007
