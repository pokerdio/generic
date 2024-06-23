

def kapow(a, b, p):
    ret = 1

    while b > 0:
        if b % 2 == 1:
            ret = (ret * a) % p
        a = a * a % p
        b //= 2
    return ret


def inverse(x, n):
    return kapow(x, n - 2, n)


def foo(n, mod=1000000007):
    f = 1
    j = 1

    La, Lb = 1, 3
    for i in range(n - 2):
        La, Lb = Lb, (La+Lb) % mod

    ret = La + Lb
    for i in range(1, n):
        if i % 100000 == 0:
            print('doin', i)
        j = j * (n - i) % mod
        if i > 1:
            j = (j * (n + i - 1)) % mod
            j = (j * inverse(n - i + 1, mod)) % mod
        j = (j * inverse(i, mod)) % mod
        ret = (ret + Lb * j) % 1000000007

        La, Lb = ((Lb-La) % 1000000007, La)
    return ret


# print(foo(10**8-1))
