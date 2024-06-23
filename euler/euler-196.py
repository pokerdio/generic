from primez import rm_prime


def friends(n, k):
    if k % 2:
        return (n - k + 1, k - 1),  (n + k - 1, k + 1), (n + k + 1, k + 1)
    else:
        return (n - k, k - 1), (n - k + 2, k - 1), (n + k, k + 1)


def isprime(x, g={}):
    if x in g:
        return g[x]
    yas = rm_prime(x)
    g[x] = yas
    return yas


def s(k):
    a, b = (k * (k - 1) // 2 + 1) | 1, k * (k + 1) // 2 + 1

    ret = 0
    for i in range(a, b, 2):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            continue
        if not rm_prime(i):
            continue

        f = friends(i, k)
        if sum(isprime(x[0]) for x in friends(i, k)) >= 2:
            ret += i
        else:
            for frend, row in f:
                if not isprime(frend):
                    continue
                if sum(isprime(x[0]) for x in friends(frend, row)) >= 2:
                    ret += i
                    break
    return ret


# print(s(5678027) + s(7208785)) # time consuming
