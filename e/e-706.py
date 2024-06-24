def testie(n):
    v = {}
    for i in range(10 ** (n - 1), 10 ** n):
        s = str(i)

        t = [0, 0, 0, 0]
        for a in range(0, len(s)):
            t[int(s[a:]) % 3] += 1

            for b in range(a + 1, len(s) + 1):
                if int(s[a:b]) % 3 == 0:
                    t[3] += 1
        for j in range(4):
            t[j] %= 3
        t = tuple(t)

        v[t] = v.get(t, 0) + 1

    return v


def go(n):
    v = {}
    for i in range(1, 10):
        k = (int(i % 3 == 0), int(i % 3 == 1), int(i % 3 == 2), int(i % 3 == 0))
        v[k] = v.get(k, 0) + 1
#    print(v)
    for _ in range(n - 1):
        v2 = {}

        for t, count in v.items():
            a0, a1, a2, threes = t

            for d in range(10):
                b = [0, 0, 0, 0]
                b[d % 3] = (a0 + 1) % 3
                b[(d + 1) % 3] = a1
                b[(d + 2) % 3] = a2
                b[3] = (threes + t[(0, 2, 1)[d % 3]] + (d % 3 == 0)) % 3
                b = tuple(b)
                v2[b] = (v2.get(b, 0) + count) % 1000000007
        v = v2
#        print(v)

    ret = 0
    for t, count in v.items():
        if t[3] == 0:
            ret += count
    return ret % 1000000007
