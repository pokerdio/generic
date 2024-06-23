def gen_a(n):
    ret = [0] * n
    for i in range(1, n):
        ret[i] = 1 - ret[i // 2] if i % 2 else ret[i // 2]
    return ret


def gen_b(n):
    ret = [0] * n

    x = 1
    for i in range(1, n):
        if (2 + 2 * i - x) ** 2 >= 5 * (x ** 2):
            x += 1
            ret[i] = 1
    return ret


def gen_b2(n):
    phi = (math.sqrt(5) + 1) / 2

    return [int((i + 1) // phi - i // phi) for i in range(n)]


assert(gen_b(1000) == gen_b2(1000))


def gen_c(n):
    a = gen_a(n)
    b = gen_b(n)

    c = [a[i] ^ b[i] for i in range(n)]
    return c


#assert(gen_c(100) == gen_c2(100))


def repsg(v, l):
    kode = 0
    minus = 2 ** l
    for i in range(l):
        kode = kode * 2 + v[i]

    g = {kode: 1}

    for i in range(l, len(v)):
        kode = kode * 2 - minus * v[i - l] + v[i]
        g[kode] = g.get(kode, 0) + 1

    return max(g.values()), g


def reps(v, l):
    kode = 0
    minus = 2 ** l
    for i in range(l):
        kode = kode * 2 + v[i]

    g = {kode: 1}

    for i in range(l, len(v)):
        kode = kode * 2 - minus * v[i - l] + v[i]
        g[kode] = g.get(kode, 0) + 1

    return max(g.values())
