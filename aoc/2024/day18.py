def getPozInts(s):
    return tuple([int(w) for w in re.findall("[0-9]+", s)])

v = [getPozInts(s) for s in open("day18_input.txt").readlines()]


if len(v) < 1024:
    WIDTH = 7
    HEIGHT = 7
    BYTE_COUNT = 12 
else:
    WIDTH = 71
    HEIGHT = 71
    BYTE_COUNT = 1024 


DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))

def path_to_exit(bytes):
    map = [[0] * WIDTH for _ in range(HEIGHT)]

    for i in range(bytes):
        x, y = v[i]
        map[y][x] = -1

    open_stack = [(0,0)]
    for idx in range(WIDTH * HEIGHT):
        if idx >= len(open_stack):
            break
        x, y = open_stack[idx]
        cost = map[y][x]

        for dx, dy in DELTA:
            x1, y1 = x+dx, y+dy
            if x1 < 0 or y1 < 0 or x1 >= WIDTH or y1 >= HEIGHT:
                continue
            if map[y1][x1] == 0:
                map[y1][x1] = cost + 1
                open_stack.append((x1, y1))
                
    foo(map)
    return map[HEIGHT-1][WIDTH-1]

print(path_to_exit(BYTE_COUNT))


def foo(map, WIDTH=WIDTH, HEIGHT=HEIGHT):
    print("\n", "\n".join("".join(f"{map[y][x]:4d}" if map[y][x] >= 0 else "####" for x in range(WIDTH)) for y in range(HEIGHT)))


for i in range(len(v)):
    if not path_to_exit(i):
        print(i, v[i-1])
        break
