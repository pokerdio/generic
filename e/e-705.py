import sieves


def make_trans():
    div = [[] for _ in range(10)]
    for i in range(1, 10):
        for j in range(1, 10):
            if i % j == 0:
                div[i].append(j)
    return div


def iterate_prime_nonzero_digitz(n):
    for p in sieves.sieve_atkin(n):
        for c in str(p):
            i = int(c)
            if i > 0:
                yield int(c)


# 1111
# 1117
# 1151
# 1157
# 1311
# 1317
# 1351
# 1357
# 2111
# 2117
# 2151
# 2157
# 2311
# 2317
# 2351
# 2357


def go(n):
    tr = make_trans()

    v = [0, 1, *([0] * 8)]
    paths = 1
    ret = 0
    k = 0
    for x in iterate_prime_nonzero_digitz(n):
        #        print(f"x={x}", ret, paths)
        k += 1
        if k % 100000 == 0:
            print(k)
        v2 = [0] * 10
        div = tr[x]  # digitz dividing x (the current digit)
        ret = (ret * len(div)) % 1000000007  # all walks so far are multiplied

        for digit in range(1, 10):
            count = v[digit]
            v2[digit] = ((count * len(div)) + (digit in div) * paths) % 1000000007
            for d in div:
                if d < digit:
                    ret = (ret + count) % 1000000007

        paths = (paths * len(div)) % 1000000007
        v = v2
#        print(v)
    return ret


print(go(10**8))
