def go(n):
    v = [{} for x in range(0, n + 1)]  # v[number of symbols] = combo count for free variable count

    v[1][1] = 1

    for i in range(4, n + 1):
        # lambda(x.m)
        if i >= 6:
            for nfree, combos in v[i - 5].items():
                v[i][nfree] = (v[i].get(nfree, 0) + combos) % 1000000007
                if nfree > 0:
                    v[i][nfree - 1] = (v[i].get(nfree - 1, 0) + combos * nfree) % 1000000007

        for j in range(1, i - 2):
            k = i - j - 2
            for nfreej, combosj in v[j].items():
                for nfreek, combosk in v[k].items():
                    combosjk = (combosj * combosk) % 1000000007
                    for joinfree, combos in application((nfreej, nfreek)):
                        v[i][joinfree] = (v[i].get(joinfree, 0) +
                                          combosjk * combos) % 1000000007

    return(sum(v[i].get(0, 0) for i in range(0, n + 1)) % 1000000007)
#    return v


def go2(n):
    v = [{} for x in range(0, n + 1)]  # v[number of symbols] = combo count for free variable count

    v[1][1] = 1

    for i in range(4, n + 1):
        print(i, "/", n)
        maxfree = (n - i) // 5

        # lambda(x.m)
        if i >= 6:
            for nfree, combos in v[i - 5].items():
                if nfree <= maxfree:
                    v[i][nfree] = (v[i].get(nfree, 0) + combos) % 1000000007
                if nfree > 0 and nfree <= maxfree + 1:
                    v[i][nfree - 1] = (v[i].get(nfree - 1, 0) + combos * nfree) % 1000000007

        # (jk)
        for j in range(1, i - 2):
            k = i - j - 2
            for nfreej, combosj in v[j].items():
                for nfreek, combosk in v[k].items():
                    combosjk = (combosj * combosk) % 1000000007
                    for joinfree, combos in application((nfreej, nfreek)):
                        if joinfree <= maxfree:
                            v[i][joinfree] = (v[i].get(joinfree, 0) + combosjk * combos) % 1000000007
                        else:
                            break

    print(sum(v[i].get(0, 0) for i in range(0, n + 1)) % 1000000007)
    return v


def application(n12, v={}):
    """application of lambda expressions with n1 and n2 free variables"""

    if (n12 in v):
        return v[n12]

    n1, n2 = n12

    ret = []
    c1 = 1
    c2 = 1
    p = 1
    for common_count in range(0, min(n1, n2) + 1):
        ret.append((n1 + n2 - common_count, (c1 * c2 * p) % 1000000007))
        c1 = c1 * (n1 - common_count) // (1 + common_count)
        c2 = c2 * (n2 - common_count) // (1 + common_count)
        p = p * (common_count + 1)
    ret = list(reversed(ret))
    v[n12] = ret
    return ret


s = """(lx.x), (lx.(x x)), (lx.(ly.x)), (lx.(ly.y)),
(lx.(x(x x))), (lx.((x x) x)), (lx.(ly.(x x))), (lx.(ly.(x y))),
(lx.(ly.(y x))), (lx.(ly.(y y))), (lx.(x(ly.x))), (lx.(x(ly.y))),
(lx.((ly.x) x)), (lx.((ly.y) x)), ((lx.x)(lx.x)), (lx.(x(x(x x)))),
(lx.(x((x x) x))), (lx.((x x)(x x))), (lx.((x(x x)) x)), (lx.(((x x) x) x))"""


s = s.replace(" ", "")
s = s.replace("\n", "")
v = s.split(",")


def subset_combos_007(n, v={}):
    if n in v:
        return v[n]

    ret = [(0, 1)]
    k = 1
    for i in range(1, n + 1):
        k = k * (n - i + 1) // i
        ret.append((i, k % 1000000007))
    v[n] = ret
    return ret


def go3(n):
    v = [{} for x in range(0, n + 1)]  # v[number of symbols] = combo count for free variable count

    v[1][1] = 1

    for i in range(4, n + 1):
        print(i)
        # lambda(x.m)
        if i >= 6:
            for nfree, combos in v[i - 5].items():
                for nfree2, combo2 in subset_combos_007(nfree):
                    v[i][nfree2] = (v[i].get(nfree2, 0) + combos * combo2) % 1000000007

        for j in range(1, i - 2):
            k = i - j - 2
            for nfreej, combosj in v[j].items():
                for nfreek, combosk in v[k].items():
                    combosjk = (combosj * combosk) % 1000000007

                    free_total = nfreej + nfreek
                    v[i][free_total] = (v[i].get(free_total, 0) + combosjk) % 1000000007

    return(sum(v[i].get(0, 0) for i in range(0, n + 1)) % 1000000007)
