v = [list(s.strip()) for s in open("day6_input.txt").readlines()]



for i in range(len(v)):
    for j in range(len(v[0])):
        if v[i][j] == "^":
            x = j
            y = i


def findLoop(v, x, y):
    dir = ((0, -1), (1, 0), (0, 1), (-1, 0))
    dir_idx = 0

    history = set((x, y, dir_idx))
    while True:
        for i in range(4):
            x1, y1 = x + dir[(dir_idx + i) % 4][0], y + dir[(dir_idx + i) % 4][1]
            if x1 < 0 or x1 >= len(v[0]) or y1 < 0 or y1 >= len(v):
                return False
            if (v[y1][x1] != "#"):
                v[y1][x1] = "^"
                x, y = x1, y1
                dir_idx = (dir_idx + i) % 4
                
                pos = (x, y, dir_idx)
                if (pos in history):
                    return True
                history.add(pos)
                break


ret = 0
for i in range(len(v)):
    print(i)
    for j in range(len(v[0])):
        if v[i][j] == ".":
            v2 = [line[:] for line in v]
            v2[i][j] = "#"
            ret += findLoop(v2, x, y)

print(ret)
