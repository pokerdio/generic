from math import log, sqrt


def make_primez(n):
    sv = [1] * (n + 1)
    for i in range(2, int(sqrt(n)) + 2):
        if sv[i]:
            for j in range(i * 2, n + 1, i):
                sv[j] = 0
    return [x for x in range(2, n + 1) if sv[x]]


def fits(part, n):
    if part[-1] >= n:
        return False
    for i in part:
        if n % i == 0:
            return False
    return True


def make23(n):
    max2 = int(log(n, 2)) + 1
    ret = []
    for two in range(max2):
        for three in range(max2):
            x = 2 ** two * 3 ** three
            if x <= n:
                ret.append(x)
            else:
                break
    return sorted(ret)


# def go(n):
#     v23 = sorted(list(make23(n)))[1:]
#     v23set = set(v23)
#     v = [[], [], [(2,)]]
#     for i in range(3, n):
#         if i % 1000 == 0:
#             print(i)
#         if i in v23set:
#             newpats = {(i,)}
#         else:
#             newpats = set()

#         for delta in v23:
#             if i > delta:
#                 for pat in v[i - delta]:
#                     if fits(pat, delta):
#                         newpats.add(tuple(sorted((*pat, delta))))
#             else:
#                 break
#         v.append(tuple(newpats))
#     return v


def go2(n):
    v23 = sorted(list(make23(n)))[1:]
    v23set = set(v23)
    v = [[], [], [(2,)]]
    for i in range(3, n):
        if i % 1000 == 0:
            print(i)
        if i in v23set:
            newpats = [(i,)]
        else:
            newpats = []

        for delta in v23:
            if i > delta:
                for pat in v[i - delta]:
                    if fits(pat, delta):
                        newpats.append(pat + (delta,))
            else:
                break
        v.append(newpats)
    return v


n = 1000000
v = go2(n)
print(sum(x for x in make_primez(n) if len(v[x]) == 1))
