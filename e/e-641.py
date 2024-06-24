import primez
from builtins import sum

vp = list(primez.iterate_primez(5*10**8))


def gen_power_combos(maxn, minp=0, vp=vp):
    yield ()
    if maxn < vp[minp] ** 4:
        return
    for i in range(4, 150, 6):
        for j in range(0, 3, 2):
            k = i + j
            v = vp[minp] ** k
            if v <= maxn:
                for combo in gen_power_combos(maxn // v, minp + 1):
                    yield (k, *combo)
            else:
                return


def combos(maxn):
    ret = []
    for c in gen_power_combos(maxn, 0):
        if sum(x % 6 == 4 for x in c) % 2 == 0:
            ret.append(c)
    return ret


def count_combo(c, minp, maxn, vp=vp):
    if not c:
        return 1
    if len(c) == 1:
        power = c[0]
        if vp[minp] ** power > maxn:
            return 0

        a = minp
        b = len(vp) - 1
        while b - a > 1:
            mid = (a + b) // 2
            if vp[mid] ** power <= maxn:
                a = mid
            else:
                b = mid
        if vp[b] ** power <= maxn:
            a = b
        return a - minp + 1

    s = sum(c)
    ret = 0
    c2 = c[1:]
    for i in range(minp, len(vp)):
        p = vp[i]
        if p ** s > maxn:
            return ret
        ret += count_combo(c2, i + 1, maxn // p ** c[0])
    return ret


def go(n):
    return sum(count_combo(c, 0, n) for c in combos(n))

# 793525366
