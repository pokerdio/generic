

from itertools import count
import primez
import math


def radset(n):
    ret = set()
    for p in primez.iterate_primez(int(math.sqrt(n)) + 4):
        while n % p == 0:
            n //= p
            ret.add(p)
            if n == 1:
                break
    if n > 1:
        ret.add(n)
    return ret


def setproduct(s):
    ret = 1
    for n in s:
        ret *= n
    return ret


def go(n):
    k = 0
    rs = [None]
    rad = [None]

    for i in range(1, n):
        rs.append(radset(i))
        rad.append(setproduct(rs[i]))

    total = 0
    for i in range(2, n):
        k, l = 0, 1
        si = rs[i]
        radi = rad[i]

        if not rs[i] & rs[i - 1]:
            if (rad[i] * rad[i - 1] < i):
                total += i

        for p in primez.iterate_primez():
            if p not in si:
                k += 1
                l *= p
            if k == 2:
                break
        idivradi = i // radi
        if idivradi >= l:
            for j in range(2, (i + 1) // 2):
                sj, radj = rs[j], rad[j]
                k = i - j
                sk, radk = rs[k], rad[k]
                if radj * radk >= idivradi:
                    continue
                if sj & sk:
                    continue
                total += i
    return total
