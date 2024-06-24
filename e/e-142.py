def sq(n):
    a = int(sqrt(n))
    return n == a * a


def go(n):
    pairs = {}

    for i in range(1, n):
        a = i * i

        for y, lst in pairs.items():
            for z in lst:
                if sq(a - y) and sq(a - z):
                    s = (a + y + z)
                    print((s - 2 * z) / 2, (s - 2 * y) / 2, (s - 2 * a) / 2, s // 2)

        for j in range(1, i):
            b = j * j
            if sq(a - b):
                if b in pairs:
                    pairs[b].append(a)
                else:
                    pairs[b] = [a]
