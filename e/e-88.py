# the 1+1+..+1+2+n = 2 * n gives a maximum value for the n terms sum product
# considering all products below this value guarantees a correct result


def visualize(func):
    level = 0

    def wrapper(*args, **kwargs):
        nonlocal level
        level += 1

        print("  >" * level, args, kwargs)
        result = func(*args, **kwargs)
        print("  <" * level)
        level -= 1
        return result
    return wrapper


def prods(minn, maxn):
    maxnsqrt = int(math.sqrt(maxn))
    for i in range(minn, maxnsqrt + 1):
        for prod in prods(i, maxn // i):
            yield [i, prod]
    for i in range(minn, maxn + 1):
        yield i


def pickrandomn(lst, n):
    ret = []
    k = 0
    for i in lst:
        if k < n:
            ret.append(i)
        else:
            j = randint(k)
            if j < n:
                ret[j] = i

        k += 1
    return ret


def testrandomn(n=8):
    test = list(range(n))
    d = {}
    for i in range(100000):
        t = tuple(pickrandomn(test, 2))
        d[t] = d.get(t, 0) + 1
    return list(sorted(d.items(), key=lambda x: x[1]))


def deepprod(lst):
    if lst == None:
        return 1
    if type(lst) == int:
        return lst
    ret = 1
    for i in lst:
        ret *= deepprod(i)
    return ret


def deepsum(lst):
    if lst == None:
        return 0
    if type(lst) == int:
        return lst
    ret = 0
    for i in lst:
        ret += deepsum(i)
    return ret


def deeplen(prod):
    ret = 0
    for i in prod:
        if type(i) == int:
            ret += 1
        else:
            ret += deeplen(i)
    return ret


def makedict(maxprod):
    d = {}
    for prod in prods(2, maxprod):
        if type(prod) == int:
            continue
        s = deepsum(prod)
        p = deepprod(prod)
        k = deeplen(prod)

        prod_elements = k + p - s  # considering how many ones it needs to make
        # the sum equal to the product
        if prod_elements in d:
            d[prod_elements] = min(d[prod_elements], p)
        else:
            d[prod_elements] = p

    return d


def go(maxn):
    d = makedict(maxn * 2)
    d = {a: b for a, b in d.items() if a <= maxn}
    if len(d) == maxn - 1:
        return sum(list(set(d.values())))


def penta(n):
    for i in range(1, n):
        yield i * (3 * i - 1) // 2
        yield -i * (3 * -i - 1) // 2


def
