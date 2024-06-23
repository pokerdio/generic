from builtins import sum
# import sys
# input_str = sys.stdin.read().split()
# input_str_idx = 0


# def pop_int():
#     global input_str_idx
#     input_str_idx += 1
#     return int(input_str[input_str_idx - 1])


# n = pop_int()
# v = [pop_int() for c in range(n)]


10

v0 = [10, 5, 4, 9, 8, 7, 6, 3, 2, 1]
v = v0.copy()


def rotate(v, a, b):
    v[a - 1:b] = v[b-1:a - 2:-1]


def pop(v):
    if len(v) == 1:
        return v, None
    if abs(v[1] - v[0]) > 1:
        return [v[0]], v[1:]
    delta = v[1] - v[0]
    i = 2
    while i < len(v):
        if v[i] - v[i - 1] != delta:
            break
        i += 1
    return v[:i], v[i:]


def split(v):
    ret = []
    while v:
        a, v = pop(v)
        ret.append((a[0], a[-1]))
    return ret


def cure(v):
    ret = [v[0]]
    for c in v[1:]:
        if abs(ret[-1][1] - c[0]) == 1:
            ret[-1] = (ret[-1][0], c[1])
        else:
            ret.append(c)
    return ret


def pairs(n):
    for i in range(n):
        for j in range(i + 1, n + 1):
            yield i, j


def twist(v, start, stop):
    v = v.copy()
    v[start:stop] = reversed([tuple(reversed(p)) for p in v[start:stop]])
    return v


def go(v):
    best = 999
    besta, bestb = 0, 0
    bestv = None
    ret = []
    for start, stop in pairs(len(v)):
        a = 1 + sum(abs(p[1] - p[0]) + 1 for p in v[:start])
        b = a + sum(abs(p[1] - p[0]) + 1 for p in v[start:stop]) - 1
        v2 = cure(twist(v, start, stop))
        score = len(v2)

        ret.append((score, v2, a, b))
    for score, v, a, b in sorted(ret):
        yield v, a, b


def rec(v, depth):
    if len(v) == 1:
        if v[0][0] == 1:
            print(depth)
            return True
        if depth < 3:
            print(depth+1)
            print(1, max(v[0]))
            return True
    if depth == 3:
        return False
    for v2, a, b in go(v):
        if rec(v2, depth + 1):
            print(a, b)
            return True


v = split(v)
rec(v, 0)
