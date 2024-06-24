def f(n, k):
    k2 = k * (k + 1) // 2
#    print(n, k, k2, n - k2)
    if n < k2:
        return 0
    return (n - k2) // k + 1


def F(n):
    return sum(f(n, k) for k in range(1, n + 1))


def S(n):
    return sum(F(i) for i in range(1, n + 1))


def Sk(n, k):
    k2 = k * (k + 1) // 2
    if n < k2:
        return 0

    full_steps = (n - k2 + 1) // k

#    print(k2, full_steps, full_steps * (full_steps + 1) // 2 * k, ((n - k2) % k) * (full_steps + 1))

    return full_steps * (full_steps + 1) // 2 * k + ((n - k2 + 1) % k) * (full_steps + 1)


def Sk2(n, k):
    return sum(f(i, k) for i in range(1, n + 1))


def S2(n):
    maxk = int(sqrt(n * 2) + 10)

    ret = 0
    print("lastk:",  Sk(n, maxk - 1))
    for k in range(1, maxk):
        if k % 1000000 == 0:
            print("%dM//%dM" % (k // 1000000, maxk // 1000000))
        ret += Sk(n, k)
    return ret


def foo(k):
    return [f(n, k) for n in range(1, 100)]


# print(S2(10**16) % 1000000007

# 929723499956693737817604096682206


def test():
    for i in range(10, 250, 13):
        print(S2(i) - S(i))
