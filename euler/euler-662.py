from math import sqrt


def gen_pairs(n):
    for i in range(1, n):
        print("pairs", i)
        for j in range(i + 1, n + 1):
            k = int(sqrt(i * i + j * j))
            if k ** 2 == i * i + j * j:
                yield i, j, k


def fibo(n):
    ret = [1, 2]
    while ret[-1] <= n:
        ret.append(ret[-1] + ret[-2])
    return ret[:-1]


problemn = 10000
v = list(gen_pairs(problemn))

fiboseq = fibo(max((x for x in v), key=lambda x: x[2])[2])
fiboset = set(fiboseq)
v2 = [(i, j) for (i, j, k) in v if k in fiboset]

for x in fiboseq:
    v2.append((0, x))
v2 = v2 + [(j, i) for (i, j) in v2]
v2 = sorted(v2, key=lambda x: x[0] + x[1])


def second_coord(x, y, n):
    return x if x + y <= n else n - y  # x - (x + y - n)


def go(n):
    v = [[0] * (n + 1 - abs(x - n)) for x in range(2 * n + 1)]
    v[0][0] = 1

    for xy in range(0, n + 1):
        print("one", xy)

        while v2[-1][0] + v2[-1][1] + xy > 2 * n:
            v2.pop()
        for x in range(0, xy + 1):
            y = xy - x
            val = v[xy][x]
            for dx, dy in v2:
                x2 = x + dx
                y2 = y + dy
                if x2 <= n and y2 <= n:
                    w2 = second_coord(x2, y2, n)
                    xy2 = x2 + y2
                    v[xy2][w2] = (v[xy2][w2] + val) % 1000000007

    for x0 in range(1, n):
        print("two", x0)
        xy = x0 + n

        while v2[-1][0] + v2[-1][1] + xy > 2 * n:
            v2.pop()
        for x in range(x0, n + 1):
            y = xy - x
            val = v[xy][x - x0]

            for dx, dy in v2:
                x2 = x + dx
                y2 = y + dy
                if x2 <= n and y2 <= n:
                    w2 = second_coord(x2, y2, n)
                    xy2 = x2 + y2
                    v[xy2][w2] = (v[xy2][w2] + val) % 1000000007

    return v[-1][0]


print(go(problemn))
