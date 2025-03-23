import re

import math

def readData(fname):
    v = [s.strip() for s in open(fname).readlines()]
    ret = {}
    for i in range(len(v)):
        for j in range(len(v[0])):
            c = v[i][j]
            if c != ".":
                if c in ret:
                    ret[c].append((j, i))
                else:
                    ret[c] = [(j, i)]
    return ret, len(v), len(v[0])

data, height, width = readData("day8_input.txt")
# data, height, width = readData("day8_example.txt")

def onMap(x, y, width, height):
    if (x >= 0 and x < width and y >= 0 and y < height):
        return True

def antiNode(x1, y1, x2, y2, width, height):
    dx = x2 - x1
    dy = y2 - y1

    if dx % 3 == 0 and dy % 3 == 0:
        x, y = x1 + dx // 3, y1 + dy // 3
        if (onMap(x, y, width, height)):
            yield (x, y)
        x, y = x1 + 2 * dx // 3, y1 + 2 * dy // 3
        if (onMap(x, y, width, height)):
            yield (x, y)

    x, y = x1 - dx, y1 - dy
    if (onMap(x, y, width, height)):
        yield (x, y)

    x, y = x2 + dx, y2 + dy
    if (onMap(x, y, width, height)):
        yield (x, y)

def problim(data, width, height, antiNodeF):
    ret = set()

    for c, v in data.items():
        if (len(v) < 2):
            continue
        for i in range(len(v) - 1):
            for j in range(i + 1, len(v)):
                for xy in antiNodeF(*v[i], *v[j], width, height):
                    ret.add(xy)
    return ret


print(len(problim(data, width, height, antiNode)))


def antiNode2(x1, y1, x2, y2, width, height):
    dx = x2 - x1
    dy = y2 - y1
    gcd = math.gcd(dx, dy)
    dx //= gcd
    dy //= gcd
    x, y = x1, y1
    while onMap(x, y, width, height):
        yield (x, y)
        x -= dx
        y -= dy
    x, y = x1+dx, y1+dy
    while onMap(x, y, width, height):
        yield (x, y)
        x += dx
        y += dy


print(len(problim(data, width, height, antiNode2)))
