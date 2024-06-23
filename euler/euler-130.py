import primez


def R(n):
    return int(str("1" * n))


def foo(n):
    r = R(n)

    for i in primez.iterate_primez(100000):
        if r % i == 0:
            while r % i == 0:
                r //= i
            yield i


def go():
    for p in range(1000000, 1100000):
        if p % 2 == 0 or p % 5 == 0:
            continue
        print("trying", p)
        k = 1
        winner = True
        for _ in range(1000000):
            k = (k * 10 + 1) % p
            if k == 0:
                winner = False
                break
        if winner:
            return p


def go():
    x = 50
    while True:
        x += 1
        if x % 2 > 0 and x % 5 > 0 and not primez.isprime(x):
            p = 1

            for _ in range(x - 2):
                p = (p * 10 + 1) % x
            if p == 0:
                yield x


gen = go()
print(sum([gen.__next__() for _ in range(25)]))
