def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = a % b, b
        a, b = max(a, b), min(a, b)
    return a


def go(n):
    ret = 0
    for a in range(1, 190):
        for b in range(a, 190):
            a2 = a * a
            b2 = b * b
            ab = (a + b) ** 2
            if gcd(a, b) > 1:
                continue
            for m in range(1, n // b2 // ab + 1):
                ra = m * ab * a2
                rb = m * ab * b2
                rc = m * a2 * b2
                if max(ra, rb, rc) <= n:
                    ret += (ra + rb + rc)
    return ret


def go2(n):
    ret = 0
    for a in range(1, 190):
        for b in range(a, 190):
            a2 = a * a
            b2 = b * b
            ab = (a + b) ** 2
            if gcd(a, b) > 1:
                continue
            m = n // b2 // ab
            ra = ab * a2
            rb = ab * b2
            rc = a2 * b2
            ret += (ra + rb + rc) * m * (m + 1) // 2
    return ret
