from collections import namedtuple as nt
#import matplotlib.pyplot as plt
import time
from builtins import sum


#from matplotlib.patches import Rectangle


def pack(v0, v1):
    if v0 > v1:
        v0, v1 = v1, v0
    return v0 * 30 + v1


def unpack(n):
    return n // 30, n % 30


S = nt("S", ["T", "L", "v", "h", "sq"])


zero = S(T=pack(1, 4), L=pack(2, 22), v=pack(11, 16), h=26, sq=14)
state_open = {zero: {pack(0, 6)}}
state_close = {}


def touches(point, s):
    """if a point touches stuff in state"""

    for i in unpack(s.T):
        if i == point or i + 1 == point or i + 6 == point:
            return True
    for i in unpack(s.L):
        if i + 1 == point or i + 6 == point or i + 7 == point:
            return True
    for i in unpack(s.v):
        if i == point or i + 6 == point:
            return True
    if s.h == point or s.h + 1 == point:
        return True
    sq = s.sq
    if sq == point or sq + 1 == point or sq + 6 == point or sq + 7 == point:
        return True


def gen_neigh(point):
    x = point % 6

    if x > 0:
        yield point - 1
    if x < 5:
        yield point + 1
    if point >= 6:
        yield point - 6
    if point < 24:
        yield point + 6


other = 666


def get_other(v, pos):
    global other
    if type(v) == int:
        v = unpack(v)
    if v[0] == pos:
        other = v[1]
        return True
    if v[1] == pos:
        other = v[0]
        return True


def replace_t(s, t0, t1):
    return S(pack(t0, t1), *s[1:])


def replace_l(s, l0, l1):
    return S(s[0], pack(l0, l1), *s[2:])


def replace_v(s, v0, v1):
    return S(*s[:2], pack(v0, v1), *s[3:])


def replace_h(s, h):
    return S(*s[:3], h, s[-1])


def replace_sq(s, sq):
    return S(*s[:-1], sq)


def sort_pair(a, b):
    return min(a, b), max(a, b)


def gen_expand(s, empty):
    # swap the first empty with a one square
    for pt in gen_neigh(empty[0]):
        if pt != empty[1] and not touches(pt, s):
            yield s, sort_pair(pt, empty[1])

    # swap the second empty with a one square
    for pt in gen_neigh(empty[1]):
        if pt != empty[0] and not touches(pt, s):
            yield s, sort_pair(pt, empty[0])

    # swap / diagonal empties
    if empty[0] % 6 and empty[0] + 5 == empty[1]:
        pos = empty[0] - 1
        # T above
        if (get_other(s.T, pos - 6)):
            yield replace_t(s, other, pos), (pos - 6, pos - 5)
        # T left
        if pos % 6 and (get_other(s.T, pos - 1)):
            yield replace_t(s, other, pos), (pos - 1, pos + 5)
        # L right
        if (pos % 6 < 5) and (get_other(s.L, pos + 1)):
            yield replace_l(s, other, pos), (pos+2, pos+8)
        # L below
        if (get_other(s.L, pos + 6)):
            yield replace_l(s, other, pos), (pos+12, pos+13)

    # swap | vertical
    if empty[0] + 6 == empty[1]:
        pos = empty[0]

        # T right
        if (pos % 6) < 5 and (get_other(s.T, pos + 1)):
            yield replace_t(s, other, pos), (pos + 2, pos + 7)
        # | right
        if (pos % 6) < 5 and (get_other(s.v, pos + 1)):
            yield replace_v(s, other, pos), (pos + 1, pos + 7)
        # | left
        if (pos % 6) and (get_other(s.v, pos - 1)):
            yield replace_v(s, other, pos), (pos - 1, pos + 5)

        # L left
        if (pos % 6) >= 2 and (get_other(s.L, pos - 2)):
            yield replace_l(s, other, pos - 1), (pos - 1, pos + 4)

        # sq left
        if (pos % 6) >= 2 and s.sq == pos - 2:
            yield replace_sq(s, pos - 1), (pos - 2, pos + 4)

        # sq right
        if (pos % 6) <= 3 and s.sq == pos + 1:
            yield replace_sq(s, pos), (pos + 2, pos + 8)

    # swap __ two spaces:
    if empty[1] % 6 and empty[0] + 1 == empty[1]:
        pos = empty[0]
        # sq above
        if s.sq == pos - 12:
            yield replace_sq(s, pos - 6), (pos - 12, pos - 11)

        # sq below
        if s.sq == pos + 6:
            yield replace_sq(s, pos), (pos + 12, pos + 13)

        # h above
        if s.h == pos - 6:
            yield replace_h(s, pos), (pos - 6, pos - 5)

        # h below
        if s.h == pos + 6:
            yield replace_h(s, pos), (pos + 6, pos + 7)

        # L above
        if get_other(s.L, pos - 12):
            yield replace_l(s, pos - 6, other), (pos - 11, pos - 6)
        # T below
        if get_other(s.T, pos + 6):
            yield replace_t(s, pos, other), (pos + 7, pos + 12)

    # h right
    if s.h % 6 and (get_other(empty, s.h - 1)):
        yield replace_h(s, s.h - 1), sort_pair(s.h + 1, other)

    # h left
    if s.h % 6 <= 3 and (get_other(empty, s.h + 2)):
        yield replace_h(s, s.h + 1), sort_pair(s.h, other)

    sv = unpack(s.v)
    for v, otherv in (sv, reversed(sv)):
        # v below
        if get_other(empty, v - 6):
            yield replace_v(s, v - 6, otherv), sort_pair(v + 6, other)

        # v above
        if get_other(empty, v + 12):
            yield replace_v(s, v + 6, otherv), sort_pair(v, other)


def remove_state(g, s, empty):
    g[s].remove(empty)
    if not g[s]:
        del g[s]


def add_state(g, s, empty):
    if s not in g:
        g[s] = {empty}
    else:
        g[s].add(empty)


def expand(s, empty):
    remove_state(state_open, s, empty)
    add_state(state_close, s, empty)
    for s1, e1 in gen_expand(s, unpack(empty)):
        e1 = pack(*e1)

        if s1 in state_close:
            sc = state_close[s1]
            if (e1 == sc) or (type(sc) == set and e1 in sc):
                continue
        add_state(state_open, s1, e1)


def go():
    last_open, last_close = 1, 0

    while state_open:
        if len(state_close) % 1000 == 0 and len(state_close) != last_close:
            print(len(state_close), len(state_open), len(state_open) - last_open)
            last_open, last_close = len(state_open), len(state_close)

        for s, e in state_open.items():
            for empty in e:
                expand(s, empty)
                break
            break
    return sum(len(empties) for empties in state_close.values())


def draw_expand(s, empty):
    for g, e in gen_expand(s, unpack(empty)):
        print(g, e)
        draw(g, pack(*e))


print(go())
