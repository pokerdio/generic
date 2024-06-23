def c(n, k, data={}):
    if n in data:
        return data[n][k]

    v = []

    q = 1
    for i in range(n):
        v.append(q % 1020202009)
        q *= n - i
        q //= i + 1

    v.append(1)
    data[n] = v
    return v[k]


def c2(n, k, data={0: [1], 1: [1, 1]}):
    print(n)
    if n in data:
        return data[n][k]

    assert(n - 1 in data)
    v = data[n - 1]
    v2 = [1]
    for i in range(n - 1):
        v2.append((v[i] + v[i + 1]) % 1020202009)

    v2.append(1)
    data[n] = v2
    return v2[k]

# horrible hack, only works for go2 only for a single run lol


def c3(n, k, data=[1, [1, 1]]):
    if n == data[0]:
        return data[1][k]

    assert(n - 1 == data[0])

    v = data[1]
    v2 = [1]
    for i in range(n - 1):
        v2.append((v[i] + v[i + 1]) % 1020202009)

    v2.append(1)
    data[0] = n
    data[1] = v2
    return v2[k]


def ctest(n):
    for i in range(2, n):
        j = i // 3

        print(i, j, c(i, j), c2(i, j))
        assert(c(i, j) == c2(i, j))


def go(n):
    v = [0, 1]

    for _ in range(n - 1):
        print(_)
        v2 = [0] * (len(v) + 1)
        for i in range(1, len(v)):
            if v[i]:
                for j in range(0, i + 1, 2):
                    ij1 = i - j + 1

                    v2[ij1] += (c2(i, j) * v[i]) % 1020202009
                    v2[ij1] %= 1020202009
        v = v2
    return sum(v) % 1020202009, v


def go2(n):
    a = [1, 1, 1]

    for nn in range(3, n + 1):
        if nn % 100 == 0:
            print(nn)
        aa = sum((c3(nn - 1, k) * a[k] * a[nn - k - 1]) % 1020202009 for k in range(nn)) * 510101005 % 1020202009
        a.append(aa)

    return aa

# go2(24680) -> 773479144
