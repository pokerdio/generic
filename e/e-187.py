import primez

p, ps = primez.init_primes(10**7 * 5)
np = len(p)


def count_primez_between(prime_idx, ceiling):
    """the low limit is given as an index in p; the high limit as a value"""
    global np
    low, high = prime_idx, np - 1

    while True:
        i = (low + high) // 2

        if p[i] <= ceiling:
            low = i
        else:
            high = i
        if p[low + 1] > ceiling:
            return low - prime_idx + 1


def count_primez_between_safe(prime_idx, ceiling):
    for i in range(prime_idx, np):
        if p[i] > ceiling:
            return i - prime_idx


def test_count_primez(n):
    global np, p, ps
    assert(np > 10000)
    assert(p[-1] > 100000)
    for i in range(n):
        idx = random.randint(1000)
        ceil = p[idx] + random.randint(40000)
        assert(count_primez_between_safe(idx, ceil) ==
               count_primez_between(idx, ceil))


s = 0

for i in range(np):
    if p[i] > 10000:
        break
    s += count_primez_between(i, 100000000 // p[i])


print(s)
