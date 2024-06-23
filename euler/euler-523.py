from itertools import permutations as perm


def mysort(v, printit=None):
    ret = v
    v = list(v)
    k = 0
    while True:
        for i in range(len(v) - 1):
            if v[i] > v[i + 1]:
                v = [v[i + 1]] + v[:i + 1] + v[i + 2:]
                k += 1
                if printit:
                    print(v)
                break
        else:
            return k, ret


def foo(n=4):
    ret = 0
    nperm = 0
    for p in perm(list(range(1, n + 1))):
        ret += mysort(p)[0]
        nperm += 1
    return ret / nperm


def x_sorted_ev(n):
    "ev of switches to sort xabcdef  where abcdef are sorted and x is random"
    if n <= 0:
        return 0.0
    ret = 0.0
    d = 1.0 / n
    for x in range(1, n):  # x rank
        ret += d * (2 ** x - 1)
    return ret


def go(n):
    ev = [0.0, 0.0, 0.5]

    for i in range(3, n + 1):
        #        print("---------", i, "--------")
        ev1 = 0.0
        d = 1.0 / i  # max number position: 0..i-1

        for big_idx in range(i):
            #            print("big_idx", big_idx)
            if big_idx > 0:
                ev1 += d * ev[big_idx]  # first sort the subarray before the big
#                print("sort before", ev[big_idx])

            for y in range(big_idx + 1, i):
                ev1 += (1.0 + x_sorted_ev(y)) * d
#                print("xsorting for ", y, ("adding %.3f" % (x_sorted_ev(y) + 1.0)))
        ev.append(ev1)

    return ev[-1]


print("%.2f" % go(30))
