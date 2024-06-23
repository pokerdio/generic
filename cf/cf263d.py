import itertools as it
# with open("a.txt") as f:
#     def input(lines=list(f.readlines())):
#         return lines.pop(0)
import sys


input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


n = pop_int()
pairs = [tuple(sorted((pop_int() - 1, pop_int() - 1))) for _ in range(n*2)]


def slow():
    for p in it.permutations(range(n)):
        for i in range(n):
            if tuple(sorted((p[i], p[(i + 1) % n]))) not in pairs:
                break
            if tuple(sorted((p[i], p[(i + 2) % n]))) not in pairs:
                break
        else:
            return p


def intersect_count(v1, v2):
    return sum(x in v2 for x in v1)


def fast():
    furbies = {x: [] for x in range(n)}
    twobies = {x: [] for x in range(n)}
    for a, b in pairs:
        furbies[a].append(b)
        furbies[b].append(a)
    if set(len(x) for _, x in furbies.items()) != {4}:
        return

    for x, fur in furbies.items():
        tx = twobies[x]
        for y in fur:
            if intersect_count(fur, furbies[y]) == 2:
                ty = twobies[y]
                if tx:
                    if y not in tx:
                        tx.append(y)
                else:
                    tx.append(y)
                if ty:
                    if x not in ty:
                        ty.append(x)
                else:
                    ty.append(x)

    if set(len(x) for _, x in twobies.items()) != {2}:
        return
    all = set(range(1, n))
    ret = [0]
    i = 0
    for _ in range(n - 1):
        for j in twobies[i]:
            if j in all:
                i = j
                break
        else:
            return
        ret.append(i)
        all.remove(i)

    if len(ret) == n:
        return ret


if n < 9:
    ret = slow()
else:
    ret = fast()

if ret:
    s = " ".join(str(x + 1) for x in ret)
    print(s)
else:
    print(-1)


def gen(n):
    with open("a.txt", "w") as f:
        f.write("%d\n" % n)
        for i in range(n):
            f.write("%d %d\n" % (i + 1, (i + 1) % n + 1))
            f.write("%d %d\n" % (i + 1, (i + 2) % n + 1))
