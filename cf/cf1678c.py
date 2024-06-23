import sys
t = int(input())


p0 = [5, 3, 6, 1, 4, 2]
p0 = [5, 1, 6, 2, 8, 3, 4, 10, 9, 7]
n0 = len(p0)


def go(n=n0, p=p0):
    v = [[0] * n for _ in range(n)]
    prefix_v = [[0] * n for _ in range(n)]
    for b in range(0, n):
        kount_smol = 0
        for d in range(n - 1, b, -1):
            if p[b] > p[d]:
                kount_smol += 1
            v[b][d] = kount_smol

    prefix_v[0] = v[0].copy()
    for b in range(1, n):
        for x in range(n):
            prefix_v[b][x] = v[b][x] + prefix_v[b - 1][x]
    ret = 0
    for a in range(0, n - 3):
        for c in range(a + 2, n - 1):
            if p[a] < p[c]:
                delta = prefix_v[c - 1][c + 1] - prefix_v[a][c + 1]
                if delta > 0:
                    ret += delta
    return ret


def go2(n=n0, p=p0):
    v = [[0] * n for _ in range(n)]
    for b in range(0, n):
        kount_smol = 0
        for d in range(n - 1, b, -1):
            if p[b] > p[d]:
                kount_smol += 1
            v[b][d] = kount_smol

    for b in range(1, n):
        for x in range(n):
            v[b][x] += v[b - 1][x]
    ret = 0
    for a in range(0, n - 3):
        for c in range(a + 2, n - 1):
            if p[a] < p[c]:
                delta = v[c - 1][c + 1] - v[a][c + 1]
                if delta > 0:
                    ret += delta
    return ret


for _ in range(t):
    n = int(input())
    s = sys.stdin.readline()

    p = [int(c) for c in s.split()]
    print(go2(n, p))
