from collections import Counter
codz = '''973A
836A
780A
985A
413A'''.split("\n")

# codz = '''029A
# 980A
# 179A
# 456A
# 379A'''.split("\n")

import re

def numOfCode(code):
    return int(re.sub("[^0-9]", "", code))

#----------------------

numXY = {"7": (0, 0), "8": (1, 0), "9": (2, 0), 
         "4": (0, 1), "5": (1, 1), "6": (2, 1), \
         "1": (0, 2), "2": (1, 2), "3": (2, 2), \
         "0": (1, 3), "A": (2, 3), " ": (0, 3)}
numKeys = "01234567890A"
dirKeys = "><^vA"

numXYrev = {b: a for a, b in numXY.items()}

dirXY = {" ": (0, 0),  "^": (1, 0), "A": (2, 0), \
         ">": (2, 1), "v": (1, 1), "<": (0, 1)}
dirXYrev = {b: a for a, b in dirXY.items()}


def validPath(xy, xyrev, start_c, path_s):
    x, y = xy[start_c]
    if start_c == " ":
        return False

    for move in path_s:
        match move:
            case ">":
                x += 1
            case "<":
                x -= 1
            case "^":
                y -= 1
            case "v":
                y += 1
        if " " == xyrev[x, y]:
            return False
    return True

def paths(xy, xyrev, start_c, end_c): 

    x0, y0 = xy[start_c]
    x1, y1 = xy[end_c]
    dx = x1 - x0
    dy = y1 - y0

    if dx < 0:
        sx = "<" * (-dx)
    else: 
        sx = ">" * dx
    if dy < 0:
        sy = "^" * (-dy)
    else: 
        sy = "v" * dy

    path = set((sx + sy + "A", sy + sx + "A"))
    ret = []
    for p in path: 
        if validPath(xy, xyrev, start_c, p):
            ret.append(p)
    return ret


def makeNumPath(start_c, end_c):
    return paths(numXY, numXYrev, start_c, end_c)

def makeDirPath(start_c, end_c):
    return paths(dirXY, dirXYrev, start_c, end_c)
    
dirPath = {(c1, c2):makeDirPath(c1, c2) for c1 in dirKeys for c2 in dirKeys}
numPath = {(c1, c2):makeNumPath(c1, c2) for c1 in numKeys for c2 in numKeys}

numTransition = {}
dirTransition = {}


def calcAll(key_depth):
    global numTransition, dirTransition
    numTransition = {}
    dirTransition = {}

    for c1 in dirKeys:
        for c2 in dirKeys:
            dirTransition[c1, c2, 0] = len(dirPath[c1, c2][0])

    for depth in range(1, key_depth):
        for c1 in dirKeys:
            for c2 in dirKeys:
                val = 0
                path = dirPath[c1, c2][0]
                last = 'A'
                for c in path:
                    val += dirTransition[last, c, depth - 1]
                    last = c
                dirTransition[c1, c2, depth] = val

    for c1 in numKeys: 
        for c2 in numKeys:
            last = 'A'
            val = 0
            for c in numPath[c1, c2][0]:
                val += dirTransition[last, c, key_depth - 1]
                last = c
            numTransition[c1, c2] = val

def calcCode(code):
    last = 'A'
    ret = 0
    for c in code: 
        ret += numTransition[last, c]
        last = c
    return ret * numOfCode(code)

def allCodes():
    return sum(calcCode(c) for c in codz)

def rotate(v):
    store = v[0]
    for i in range(len(v) - 1):
        v[i] = v[i + 1]
    v[-1] = store
    return v

def problim(depth):
    calcAll(depth)
    current_val = allCodes()
    ok = True
    while ok:
        ok = False
        for keys, path in ((numKeys, numPath), (dirKeys, dirPath)):
            for c1 in keys:
                for c2 in keys:
                    p = path[c1, c2]
                    best_rotation = p
                    if len(p) >= 2:
                        for _ in range(len(p)): 
                            rotate(p)
                            calcAll(depth)
                            new_val = allCodes()
                            if new_val < current_val:
                                current_val = new_val  #update best
                                ok = True
                                best_rotation = p[:]
                    path[c1, c2] = best_rotation

    return current_val

print(problim(2))
print(problim(25))
