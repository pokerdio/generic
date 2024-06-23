# b2 = q2+p2 + pq
# a2 = q2+r2 + rq
# c2 = p2+r2 + pr
##
##


#(q+p)2 - pq


# run euler-143.c first

def foo(n):
    sq = set(x * x for x in range(n + 1))
    for a in range(1, n):
        for b in range(a, n):
            if a * a + b * b + a * b in sq:
                yield a, b


def foo():
    for s in open("euler-143.txt").readlines():
        yield tuple(int(c) for c in s.strip().split(" "))


def bar():
    g = {}
    v = set()
    for p, q in foo():
        if p in g:
            g[p].append(q)
        else:
            g[p] = [q]
        v.add((p, q))
    for p, q in v:
        for t in g[p]:
            if t > p and t < q:
                if (t, q) in v:
                    if p + q + t <= 120000:
                        a, b, c = goo(p, t), goo(t, q), goo(p, q)
                        print(a, b, c, "-", p, q, t, "-", p + q + t)
                        yield p + q + t


print(sum(list(set(bar()))))
