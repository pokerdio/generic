import primez


def go(n=10**8):
    ret = 2
    for p in primez.iterate_primez(n + 1):
        pp = p
        while pp * p < n:
            pp *= p
        ret = ret * pp % 1000000007
    return ret
