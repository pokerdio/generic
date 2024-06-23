import primez


def go(n, m):
    s = {1}
    for p in primez.iterate_primez(n + 1):
        k = p
        s2 = set()
        for i in range(m):
            for j in s:
                if j * k <= m:
                    s2.add(j * k)
            k *= p
            if k > m:
                break
        s.update(s2)
    return len(s)
