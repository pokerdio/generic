from primez import decompose, iterate_primez
import primez


def mul(dec1, dec2):
    """multiply decomposition formatted numbers"""
    for i in dec2.keys():
        dec1[i] = dec1.get(i, 0) + dec2[i]


def div(dec1, dec2):
    """divide decomposition formatted numbers"""
    for i in dec2.keys():
        dec1[i] -= dec2[i]
        if not dec1[i]:
            dec1.pop(i)


def powseries(p, q, mod=1000000007):
    """1 +p + p**2 + ... + p ** q"""
    if q == 0:
        return 1
    if q == 1:
        return (p + 1) % mod

    s = primez.rm_prime_kapow(p, q + 1, mod) - 1
    q = primez.rev(p - 1, mod)
    return (s * q) % mod  # please prime mod


def D2(n, total, fact, mod=1000000007):
    """fact is factorial of n-1 in decompose format
    total is B(n-1) in decompose format
    we multiply B(n-1)with n**(n-1) and divide by factorial(n) 
    to get B(n)"""
    ndec = decompose(n)

    mul(fact, ndec)

    for i in ndec.keys():
        ndec[i] = ndec[i] * n

    mul(total, ndec)
    div(total, fact)
#    print("fuck this", total, fact)
    ret = 1
    for pr, pow in total.items():
        ret = (ret * powseries(pr, pow)) % mod
    return ret


def D(n, dec=[decompose(i) for i in range(20001)], last=[]):
    total = {}
    v = {}
    for i in range(1, n):
        mul(v, dec[n + 1 - i])
        div(v, dec[i])

        mul(total, v)
#    print("fuck this", total)
    ret = 1
    for pr, pow in total.items():
        k = 1
        q = 1
        for _ in range(1, pow + 1):
            k = (k * pr) % 1000000007
            q += k
        ret = (ret * q) % 1000000007
    return ret


def S(n):
    ret = 0
    for k in range(1, n + 1):
        print(k)
        ret = (ret + D(k)) % 1000000007
    return ret


def S2(n):
    ret = 1
    fact = {}
    b = {}
    for k in range(2, n + 1):
        print(k)
        ret = (ret + D2(k, b, fact)) % 1000000007
    return ret
