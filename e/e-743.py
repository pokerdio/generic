def f(n):
    ret = 1
    for i in range(2, n + 1):
        ret *= i
    return ret


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b // a) * x, x)


def rev(n, mod):
    _, x, _ = egcd(n, mod)
    return x % mod


def go(k, n, mod=1000000007):
    assert(n % k == 0)
    n //= k

    onetwo = (2 ** n) % mod
    twotwo = (onetwo * onetwo) % mod

    two = k % 2 and onetwo or 1
    twos = []
    for _ in range(k % 2, k + 1, 2):
        twos.append(two)
        two = (two * twotwo) % mod

    # k! // (two!**2 (k-2*two)!)

    one_two_comboz = 1  # starts with zero twos, so one combo of 1111...

    total = 0
    for two in range(0, k // 2 + 1):
        one = k - two * 2
        one_comboz = twos.pop()
        total += one_comboz * one_two_comboz
#        print(two, one, one_comboz, one_two_comboz, total)
        total %= mod

        one_two_comboz *= (k - 2 * two) * (k - 2 * two - 1)
        one_two_comboz %= mod

#        print("new_one_two_comboz", one_two_comboz)
        div_amount = ((two + 1) ** 2) % mod
        one_two_comboz = (one_two_comboz * rev(div_amount, mod)) % mod
#        print("after div: ", one_two_comboz)

    return total
