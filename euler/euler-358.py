from primez import rm_prime, rm_prime_kapow as kapow


def make_primez():
    small, big = (100000000000 // 138 | 1), 100000000000 // 137
    for i in range(small, big, 2):
        if i % 1000000 < 2:
            print(i)
        if not i % 2 or not i % 3 or not i % 5 or not i % 7 or not i % 11:
            continue
        if rm_prime(i):
            yield i

# 00000000137


def take_n(p, n, after=0):
    ret = 10
    for _ in range(n):
        yield ret // p
        ret = ((ret % p) * 10)


def take_n(p, n, start=1):
    ret = kapow(10, start - 1, p) * 10
    for _ in range(n):
        yield ret // p
        ret = ((ret % p) * 10)


def rep(p, max=1000):
    v = set()
    x = 10
    for k in range(min(p, max)):
        pair = (x % p) * 10, x // p
        x, y = pair

        if pair in v:
            return k
        v.add(pair)

# vvv = list(make_primez())


def go(vvv=vvv):
    k = 0
    for p in vvv:
        if k != p // 10000000:
            k = p // 10000000
            print(p)

        if tuple(take_n(p, 5, p - 5)) != (5, 6, 7, 8, 9):
            continue
        if tuple(take_n(p, 16, (p + 1) // 2 - 5)) != (4, 3, 2, 1, 0, 9, 9, 9, 9, 9, 9, 9, 9, 8, 6, 2):
            continue
        if tuple(take_n(p, 11)) != (0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 7):
            continue

        t1 = tuple(take_n(p, 66666, p // 3))
        t2 = tuple(take_n(p, 66666, (p - 1) // 2 + p // 3))

        for i in range(len(t1)):
            if t1[i] + t2[i] != 9:
                continue
        yield p


#vvv = [725509891, 726509891, 729809891]

# print(list(go(make_primez())))
