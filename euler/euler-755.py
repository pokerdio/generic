
def fibo(n):
    ret = [1, 2]
    sum = [1, 3]
    for i in range(n):
        ret.append(ret[-1] + ret[-2])
        sum.append(sum[-1] + ret[-1])
    return ret, sum


maxn = 70
fiboseq, fibosum = fibo(maxn)
all_combos = [2 ** (x + 1) for x in range(maxn + 1)]


def rec_counter(f):
    depth = [0]
    counter = [0]

    def innerf(*args):
        if depth[0] == 0:
            counter[0] = 0
        depth[0] += 1
        ret = f(*args)
        counter[0] += 1
        depth[0] -= 1
        if depth[0] == 0:
            print("total recursive function calls: ", counter[0])
        return ret
    return innerf


def rec_dec(f):
    depth = [0]

    def innerf(*args):
        depth[0] += 1
        print("-->" * depth[0] + " entering (" + str(args) + ")")
        ret = f(*args)
        print("-->" * depth[0] + " returning " + str(ret))
        depth[0] -= 1
        return ret
    return innerf


@rec_dec
def fiborec(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return fiborec(n - 1) + fiborec(n - 2)


# @rec_dec
# @rec_counter
def go(n, f=maxn - 1):
    """how many combo sums from the first f fibo numbers no bigger than n?"""
    if n == 0:
        return 1
    if n >= fibosum[f]:
        return all_combos[f]
    while fiboseq[f] > n:
        f -= 1
    if f == 0:
        return 1

    with_combos = go(n - fiboseq[f], f - 1)
    without_combos = go(n, f - 1)
    return with_combos + without_combos


# print(go(10**13))
