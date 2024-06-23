import matrix


def st(n, N):
    f1, f2 = 1, 1
    while n > 0:
        if f1 > f2:
            yield f2, f1
        elif f1 <= f2:
            yield f1, f2
        f1, f2 = (f1 + f2) % N, (f2 * 2 + f1) % N
        n -= 1


def value2(x, a, y, b):
    plus = 1 if a < b else -1
    s = 0
    for i in range(x, y + 1):
        s += a * i
        a += plus

    return s


def value(x, a, y, b):
    plus = 1 if a < b else -1

    #      x  a  p  s  1
    mx = [[1, 0, 0, 0, 1],
          [0, 1, 0, 0, plus],
          [plus, 1, 1, 0, plus],
          [0, 0, 1, 1, 0],
          [0, 0, 0, 0, 1]]

    mx = matrix.pow(mx, y - x + 1, 10**9)
    v = matrix.mul(mx, [x, a, a * x, 0, 1], 10**9)
    return v[3]


def go(N, K):
    v = [(0, 0, N - 1, N - 1)]

    kount = 0
    for s, t in st(K, N):
        kount += 1
        if kount % 1000 == 0:
            print("%d/%d" % (kount, K))
        xp = []
        for i in range(len(v)):
            x, a, y, b = v[i]
            plus = 1 if a < b else -1
            if y < s or x > t:
                continue
            if x < s:
                xp.append(((x, a, s - 1, (s - 1 - x) * plus + a)))
                a = (s - x) * plus + a
                x = s

            if y > t:
                xp.append((t + 1, b - (y - (t + 1)) * plus, y, b))
                b = b - (y - t) * plus
                y = t

            v[i] = t - (y - s), b, t - (x - s), a

            if x == s and y == t:
                break
        v.extend(xp)

#        print(s, t, v)

    s = 0
    tests = 0
    for x, a, y, b in v:
        tests += (y - x + 1)
        s += value(x, a, y, b)
        s %= 10**9

#    print(tests, N, len(v))

    return s
