import primez


def r1000(p):
    k = 1111
    for _ in range(166):
        k = (k * 1000000 + 111111) % p
    return k


def ten1000(p):
    k = 1
    for _ in range(200):
        k = (k * 100000) % p
    return k


def go():
    ret = set()
    for p in primez.iterate_primez():
        if 10 % p > 0:
            r = r1000(p)
            t = ten1000(p)
            r2 = r
            t2 = t
            for _ in range(999):
                r2 = ((r2 * t) + r) % p
                t2 = (t2 * t) % p
            r, t = r2, t2
            for _ in range(999):
                r2 = ((r2 * t) + r) % p
                t2 = (t2 * t) % p
            if r2 == 0:
                ret.add(p)
                print(p, len(ret))
                if len(ret) == 40:
                    return ret


# this solves for n = 1 billion only, but I don't care!

print(sum(list(go())))
