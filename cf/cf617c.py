from math import sqrt


def ints():
    return [int(x) for x in input().split()]


n, x1, y1, x2, y2 = ints()
flowers = [ints() for _ in range(n)]
r1, r2 = 0.0, 0.0


def dist(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)


flowers = sorted(flowers, key=lambda xy: dist(xy[0], xy[1], x1, y1))
best = max(dist(*xy, x2, y2) for xy in flowers) ** 2
flowers.append([x2, y2])

for i in range(n):
    r1 = dist(x1, y1, *flowers[i])
    r2 = max(dist(*flowers[j], x2, y2) for j in range(i + 1, n + 1))
    best = min(r1 * r1 + r2 * r2, best)

print(int(best + 0.25))
