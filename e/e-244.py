def expand(rb, white):
    if white % 4 < 3:
        yield (rb, white + 1), "L"
    if white % 4 > 0:
        yield (rb, white - 1), "R"
    if white > 3:
        yield (rb[:white - 4] + rb[white - 3:white] +
               rb[white - 4:white - 3] + rb[white:], white - 4), "D"

    if white < 12:
        yield (rb[:white] + rb[white + 3:white + 4] +
               rb[white:white + 3] + rb[white + 4:], white + 4), "U"


def test(white):
    return tuple(x for x in range(16) if x != white)


def pathcode(path):
    checksum = 0
    for c in path:
        checksum = (checksum * 243 + ord(c)) % 100000007
    return checksum


def go(start, stop):

    v = {start: [""]}

    banned = set()
    while stop not in v:
        v2 = {}
        for pos, paths in v.items():
            for newpos, direction in expand(*pos):
                if newpos not in banned:
                    if newpos in v2:
                        v2[newpos] += [path + direction for path in paths]
                    else:
                        v2[newpos] = [path + direction for path in paths]
        banned |= set(v2.keys())
        v = v2

    return sum(pathcode(path) for path in v[stop])


def solve():
    return go(("rbbrrbbrrbbrrbb", 0), ("brbbrbrrbrbbrbr", 0))


print(solve())
