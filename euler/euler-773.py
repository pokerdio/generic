import primez as pz


def foo(n=97):
    ret = [2, 5]
    for p in pz.ip(n * 200):
        if p % 10 == 7:
            ret.append(p)
        if len(ret) == n:
            return ret
