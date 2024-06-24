from itertools import islice


def foo(k=-1):
    for i in range(100001, 999999, 11):
        k -= 1
        if k == 0:
            return
        a = [int(x) for x in str(i)]

        print((a[0] + a[2] + a[4] - a[1] - a[3] - a[5]) % 11)


def gen(n, mod11, remain={i: 2 for i in range(10)}):
    for i in remain.keys():
        j = remain[i]
        if n == 1:
            if (i + mod11) % 11 == 0:
                yield (i,)
                return  # only one digit can fit at the end
            continue

        r2 = {a: b for a, b in remain.items() if a <= i}

        r2[i] -= 1
        if not r2[i]:
            del r2[i]

        for c in gen(n - 1, (mod11 + i) % 11, r2):
            yield (i, *c)


def go(mod11):
    fact = [1, 1]
    for i in range(2, 11):
        fact.append(i * fact[-1])
    s = 0
    for c in gen(10, 11 - mod11):
        # even digitz = ones including the lsd (last digit, least significant)
        if ((90 - sum(c)) % 11 != mod11):
            continue  # a num is 11 divisible iff sum of odd digits equals sum of even ones mod 11
        even_twos = sum(c.count(k) == 2 for k in range(10))
        even_combos = fact[10] // 2 ** even_twos

        # odd digitz = ones including the msd (first digit) that needs to be nonzero
        odd_zeros = 2 - c.count(0)
        odd_twos = sum(c.count(k) == 0 for k in range(10))
        odd_nonzero_twos = odd_twos - (odd_zeros == 2)
        odd_nonzero_ones = 10 - 2 * odd_nonzero_twos - odd_zeros

        odd_combos = 0
        if odd_nonzero_ones:
            odd_combos += odd_nonzero_ones * (fact[9] // 2 ** odd_twos)
        if odd_nonzero_twos:
            odd_combos += odd_nonzero_twos * (fact[9] // 2 ** (odd_twos - 1))

#        print(c, sum(c),  "even_twos", even_twos, "odd_zeros", odd_zeros, "odd_twos", odd_twos,
#              "odd_nonzero_twos", odd_nonzero_twos, "odd_nonzero_ones", odd_nonzero_ones)

        s += odd_combos * even_combos
    return s


print(sum(go(x) for x in range(11)))
print(go(1))
