from math import gcd

n = int(input())


def foo(n):
    best = [0, 0, 0, 0]

    for i in range(max(1, n - 20), n-1):
        for j in range(i+1, n):
            if gcd(i, j) > 1:
                continue
            for k in range(j+1, n+1):
                if gcd(i, k) == 1 and gcd(j, k) == 1:
                    q = i * j * k
                    if q > best[0]:
                        best = [q, i, j, k]
    return best


if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(foo(n)[0])
