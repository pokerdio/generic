def getInts(s):
    while True:
        match = re.search("-?[0-9]+", s)
        if not match:
            return
        sp = match.span()
        yield int(s[sp[0]:sp[1]])
        s = s[sp[1]:]

quad = [0, 0, 0, 0]

WIDTH = 101
HEIGHT = 103
TIME = 100

robots = []

for line in open("day14_input.txt").readlines():
    x, y, vx, vy = (getInts(line))
    robots.append((x, y, vx, vy))
    x = (x + vx * TIME) % WIDTH
    y = (y + vy * TIME) % HEIGHT
    if x < WIDTH // 2:
        if y < HEIGHT // 2:
            quad[0] += 1
        if y > HEIGHT // 2:
            quad[1] += 1
    if x > WIDTH // 2:
        if y < HEIGHT // 2:
            quad[2] += 1
        if y > HEIGHT // 2:
            quad[3] += 1

print(quad[0] * quad[1] * quad[2] * quad[3])



def lonelyBotCount(n):
    s = [[False] * WIDTH for _ in range(HEIGHT)]
    for x, y, vx, vy in robots:
        x = (x + vx * n) % WIDTH
        y = (y + vy * n) % HEIGHT
        s[y][x] = True

    ret = 0
    for x in range(1, WIDTH-1):
        for y in range(1, HEIGHT-1):
            if s[y][x] and not s[y-1][x] and not s[y+1][x] and not s[y][x-1] and not s[y][x+1]:
                ret += 1
    return ret

v = [lonelyBotCount(x) for x in range(10000)]
print(v.index(min(v)))

def step(n):
    s = [["."] * WIDTH for _ in range(HEIGHT)]
    for x, y, vx, vy in robots:
        x = (x + vx * n) % WIDTH
        y = (y + vy * n) % HEIGHT
        s[y][x] = "#"

    print("\n".join("".join(line) for line in s))

from time import sleep

def go():
    for n in range(1000):
        step(n)
        print(n)
        sleep(0.3)
