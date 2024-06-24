

def d(n):
    a = "141592653589793238462643383279502884197169399375105820974944592307\
8164062862089986280348253421170679"
    b = "82148086513282306647093844609550582231725359408128481117\
45028410270193852110555964462294895493038196"

    # a = "a" * 10
    # b = "b" * 10
    ab = a + b
    v = [len(a), len(b)]

    while v[-1] < n:
        v.append(v[-1] + v[-2])

    print(v)
    while len(v) > 3:
        print(n, v)
        if n > v[-3]:
            n -= v[-3]
            v.pop()
        else:
            v.pop()
            v.pop()
    print(n, v)

    if len(v) == 3:
        return ab[n - 1]
    elif len(v) == 2:
        return b[n - 1]
    else:
        return a[n - 1]


print("".join(reversed(list(d((127 + 19 * n) * (7**n)) for n in range(18)))))
