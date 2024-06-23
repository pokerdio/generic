import sys

input = sys.stdin.readline


def gen_input():
    while True:
        yield [int(c) for c in input().split()]


def gen_fake1():
    yield [5, 5, 1]
    yield [1, 2]
    yield [2, 3]
    yield [1, 4]
    yield [4, 3]
    yield [3, 5]


def gen_fake():
    yield [3, 3, 2]
    yield [1, 2]
    yield [2, 3]
    yield [3, 1]


def gen_fake3():
    yield [5, 5, 1]
    yield [1, 2]
    yield [2, 3]
    yield [3, 4]
    yield [2, 5]
    yield [5, 4]


def ints(g=gen_input()):
    return next(g)


n, m, s = ints()
s -= 1
v = [[] for _ in range(n)]

for _ in range(m):
    a, b = ints()
    v[a - 1].append(b - 1)


def down(v, s, q):
    """nodes reachable from s through q"""
    n = len(v)
    vis = [False] * n
    vis[s] = True
    back = [-1] * n
    back[q] = s
    op = [q]  # open nodes

    ret = set()
    while op:
        x = op.pop()
        ret.add(x)
        vis[x] = True
        for y in v[x]:
            if not vis[y]:
                op.append(y)
                back[y] = x
    return ret, back


def backtrack(back, start):
    ret = []
    while start != -1:
        ret.append(start)
        start = back[start]
    return list(reversed(ret))


def prune_common(path1, path2):
    for i, node in enumerate(path1):
        if i and node in path2:
            return path1[:i+1], path2[:path2.index(node) + 1]
    return path1, path2


def go(v=v, s=s):
    n = len(v)
    vis = [-1] * n
    vis[s] = s

    back = [-1] * n
    for q in v[s]:
        if vis[q] >= 0:
            return [s, q], backtrack(back, q)
        op = [q]
        back[q] = s
        while op:
            x = op.pop()
            vis[x] = q
            for y in v[x]:
                if vis[y] == -1:
                    op.append(y)
                    back[y] = x
                elif vis[y] != s and vis[y] >= 0 and vis[y] != q:
                    return backtrack(back, y), backtrack(back, x) + [y]


# def go():
#     if len(v[s]) <= 1:
#         return
#     d = [0] * len(v[s])
#     d[0] = down(v, s, v[s][0])[0]
#     vis_total = d[0]
#     for i in range(1, len(d)):
#         d[i] = down(v, s, v[s][i])[0]
#         vis_new = vis_total | d[i]
#         if len(vis_new) < len(vis_total) + len(d[i]):
#             break
#         vis_total = vis_new
#     else:
#         return

#     for j in range(0, i):
#         s12 = d[i] & d[j]
#         if s12:
#             desto = s12.pop()
#             back1 = down(v, s, v[s][i])[1]
#             back2 = down(v, s, v[s][j])[1]

#             path1 = backtrack(back1, desto)
#             path2 = backtrack(back2, desto)
#             #print(path1, path2)
#             path1, path2 = prune_common(path1, path2)
#             path1 = [x+1 for x in path1]
#             path2 = [x+1 for x in path2]
#             return path1, path2

def array_plus1(v):
    for i in range(len(v)):
        v[i] += 1


p12 = go()

if p12:
    print("Possible")
    p1, p2 = p12
    array_plus1(p1)
    array_plus1(p2)

    print(len(p1))
    print(*p1)
    print(len(p2))
    print(*p2)
else:
    print("Impossible")
