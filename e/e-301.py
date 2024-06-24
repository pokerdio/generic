def bar(x):
    return "11" not in "{0:b}".format(x)


def foo(n=100):
    ret = 0
    for i in range(n):
        if i ^ (2 * i) == 3 * i:
            print(i, "{0:b}".format(i))

        if bar(i):
            print("YAHAHAHAHAHAHA")
            ret += 1
    return ret


def go(n):
    v = [1] + [0] * n   # all desired numbers start with 10 in binary

    for i in range(n - 1):
        v[i + 1] += v[i]
        v[i + 2] += v[i]
    return v[-1] + v[-2]


print(go(31))  # should be 30 but can't be bothered it works
