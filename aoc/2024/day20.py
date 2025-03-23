map = [s.strip() for s in open("day20_input.txt").readlines()]
#map = [s.strip() for s in open("day20_example.txt").readlines()]

width = len(map[0])
height = len(map)

for y in range(len(map)):
    s = map[y]
    if "S" in s:
        startx = s.index("S")
        starty = y
        map[y] = s.replace("S", ".")
    if "E" in s:
        endx = s.index("E")
        endy = y
        map[y] = s.replace("E", ".")


def bfs():
    best = [[0] * width for _ in range(height)]
    open_lst = [(startx, starty)]
    best[starty][startx] = 1

    while open_lst: 
        pos = open_lst.pop()
        x, y = pos
        cost = best[y][x]

        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            x1, y1 = x + dx, y + dy
            if x1 < 0 or y1 < 0 or x1 >= width or y1 >= width:
                continue
            if map[y1][x1] == '.' and best[y1][x1] == 0:
                best[y1][x1] = cost + 1
                open_lst.append((x1, y1))
    return best

def count_cheats(delta, cost, max_cheat):
    ret = 0
    for x in range(width):
        for y in range(height):
            val_xy = cost[y][x]
            if val_xy == 0:
                continue
            for dx in range(-max_cheat, max_cheat + 1):
                for dy in range(-max_cheat, max_cheat + 1):
                    if abs(dx) + abs(dy) > max_cheat:
                        continue
                    cheat_cost = abs(dx) + abs(dy)
                    
                    x1, y1 = x + dx, y + dy
                    if x1 < 0 or y1 < 0 or x1 >= width or y1 >= width:
                        continue

                    val_xy1 = cost[y1][x1]
                    if val_xy1 == 0:
                        continue
                    
                    if val_xy1 - val_xy - cheat_cost >= delta:
                        #print(x, y, x1, y1, val_xy1 - val_xy - 2)
                        ret += 1
    return ret

def problim():
    cost = bfs()
    return count_cheats(100, cost, 2), count_cheats(100, cost, 20)
