v = [s.strip() for s in open("day4_input.txt").readlines()]


def findCount(s, sub):
    ret = 0
    first = 0
    while True:
        first = s.find(sub, first) + 1
        if first > 0:
            ret += 1
        else:
            return ret

def horiz(v):
    rev = ["".join(reversed(list(s))) for s in v]
    return sum(findCount(s, "XMAS") for s in v) + \
        sum(findCount(s, "XMAS") for s in rev) 


def vert(v):
    v2 = ["" for i in range(len(v[0]))]
    for j in range(len(v[0])):
        for i in range(len(v)):
            v2[j] += v[i][j]
    return horiz(v2)

def diag1(v):
    n = len(v[0])
    empty = " " * n
    v2 = [empty[i:] + v[i] + empty[:i] for i in range(len(v))]
    return vert(v2)


def diag2(v):
    n = len(v[0])
    empty = " " * n
    v2 = [empty[:i] + v[i] + empty[i:] for i in range(len(v))]    
    return vert(v2)


print(horiz(v) + vert(v) + diag1(v) + diag2(v))


def mas(v, i, j):
    if v[i][j] != "A":
        return False
    if "".join(sorted([v[i-1][j-1], v[i+1][j+1]])) != "MS":
        return False
    if "".join(sorted([v[i-1][j+1], v[i+1][j-1]])) != "MS":
        return False
    return True

def allMas(v):
    ret = 0
    
    for i in range(1, len(v) - 1):
        for j in range(1, len(v[0]) - 1):
            ret += mas(v, i, j)
    return ret

print(allMas(v))
