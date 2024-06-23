from fractions import Fraction as F


def foo(n):
    v = [set((F(1),))]

    for i in range(2, n + 1):
        v2 = set((F(i), F(1, i)))
#        print("hello", i, len(v))
        for j in range(1, len(v) // 2 + 1):
            #            print(i, j, len(v) - j)
            for a in v[j]:
                for b in v[len(v) - j]:
                    v2.add(a + b)
                    v2.add(1 / (1 / a + 1 / b))

#        print(v2)
        v.append(v2)
    return len(v[-1])


# foo(8) -> 6931
# foo(9) -> 30179
# foo(10) -> 134667 (slowish)
# 11->611339

def make(v, total, value=F(0), max=None):
    if not max:
        max = total
    for i in range(3, total)


def foo(n):
    par = [[] for _ in range(n + 1)]
    res = [[] for _ in range(n + 1)]

    par[1].append(Fr(1))
    for i in range(2, n + 1):
