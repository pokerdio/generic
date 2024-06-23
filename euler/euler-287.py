def belch(x0, y0, x1, y1, half):
    if x0 == x1:
        return 2

    """the coords gonna be inclusive 0,0,1,1 is a 2 length square"""
    minx, maxx = sorted(((x0 - half) ** 2, (x1 - half) ** 2))
    miny, maxy = sorted(((y0 - half) ** 2, (y1 - half) ** 2))

    mincolor = (minx + miny <= half * half)
    maxcolor = (maxx + maxy <= half * half)

    if mincolor == maxcolor:
        return 2

    x2 = (x0 + x1) // 2
    y2 = (y0 + y1) // 2

    return 1 + belch(x0, y0, x2, y2, half) +\
        belch(x0, y2 + 1, x2, y1, half) +\
        belch(x2 + 1, y0, x1, y2, half) +\
        belch(x2 + 1, y2 + 1, x1, y1, half)


def solve(n):
    s = 1
    half = 2 ** (n - 1)

    s += belch(0, 0, half - 1, half - 1, half)
    s += belch(0, half, half - 1, half * 2 - 1, half)
    s += belch(half, 0, half * 2 - 1, half - 1, half)
    s += belch(half, half, half * 2 - 1, half * 2 - 1, half)
    return s


# print(solve(24))
