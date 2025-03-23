v = [[int(c) for c in list(line.strip())] for line in open("day8_input.txt").readlines()]
vis = [[False for _ in range(len(v[0]))] for _ in range(len(v))]



def inside(x, y, v):
    return x >= 0 and y >= 0 and x < len(v[0]) and y < len(v)

def run(x, y, dx, dy, v, vis):
    min_vis = -1

    while inside(x, y, v):
        if v[y][x] > min_vis:
            vis[y][x] = True
            min_vis = v[y][x]
        x += dx
        y += dy

def do_vis(v, vis):
    w = len(v[0])
    h = len(v)

    for x in range(w):
        run(x, 0, 0, 1, v, vis)
        run(x, h-1, 0, -1, v, vis)
    for y in range(h):
        run(0, y, 1, 0, v, vis)
        run(w-1, y, -1, 0, v, vis)

    
        
do_vis(v, vis)
print(sum(sum(line) for line in vis))


def scenic_run(x, y, dx, dy, v):
    ret = 0
    h0 = v[y][x]

    while True:
        x += dx
        y += dy
        if not inside(x, y, v):
            return ret
        ret += 1
        if v[y][x] >= h0:
            return ret

def scenic_score(x, y, v):
    return scenic_run(x, y, 0, 1, v) * scenic_run(x, y, 0, -1, v) * \
        scenic_run(x, y, 1, 0, v) * scenic_run(x, y, -1, 0, v) 

highscore = 0

print(max(max(scenic_score(x, y, v) for x in range(len(v[0]))) for y in range(len(v))))
