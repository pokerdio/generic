import itertools as it


def foo(rgb):
    if not rgb:
        yield "r"
        yield "g"
        yield "b"

    else:
        for s in foo(rgb[1:]):
            for i in "rgb":
                for j in "rgb":
                    if i != j and j != rgb[0] and j != s[0]:
                        yield i + j + s


def bar(n):
    v = {x[::2]: 1 for x in (foo("r"))}
    v["rr"] += 1  # fuck you :D
    for _ in range(n - 2):
        v2 = {}
        for s, k in v.items():
            for s2 in foo(s):
                s3 = s2[0::2]
                v2[s3] = v2.get(s3, 0) + k
        v = v2
    return v


def go(n):
    return sum(list(bar(n).values()))


def all(n):
    for p in it.product(*(["rgb"] * n)):
        for i in range(len(p) - 1):
            if p[i] == p[i + 1]:
                break
        else:
            yield "".join(p)


def brute(n):
    if n == 1:
        yield ["r"]
        return
    doublepairs = (("r", "r"), ("g", "g"), ("b", "b"))
    for smol in brute(n - 1):
        last = smol[-1][::2]
        for new in all(n * 2 - 1):
            for pairs in zip(last, new[1::2]):
                if pairs in doublepairs:
                    break
            else:
                yield smol + [new]


def brute_signature(n):
    ret = {}
    for p in brute(n):
        s = p[-1][1::2]
        ret[s] = ret.get(s, 0) + 1
    return ret


print(go(8) * 3)
