
import itertools
import primez


def iterate_repeating_ancillary(digit, nrepeating, nfree):
    powers_of_ten = [10 ** i for i in range(nrepeating + nfree)]
    max_ten = max(powers_of_ten)
    base = sum(powers_of_ten)

    digit_lists = [[x * d for d in range(10)] for x in powers_of_ten]
    digit_lists[-1].remove(0)
    for lst in itertools.combinations(digit_lists, nfree):
        retbase = (base - sum((max(x) for x in lst)) // 9) * digit
        yield retbase, lst


def iterate_repeating(digit, nrepeating, nfree):
    if digit == 0:
        if nfree == 0:
            return
        zerobase = [(10 ** (nrepeating + nfree - 1)) * x for x in range(1, 10)]
        for base, lst in iterate_repeating_ancillary(digit, nrepeating, nfree - 1):
            for combo in itertools.product(zerobase, *lst):
                yield int(base + sum(combo))
    else:
        for base, lst in iterate_repeating_ancillary(digit, nrepeating, nfree):
            for combo in itertools.product(*lst):
                yield int(base + sum(combo))


def isprime(n, max_root):
    for p in primez.iterate_primez(max_root):
        if n % p == 0:
            return False
    return True


def get_primez_digit(digit, nrepeating, nfree):
    max_prime = int(sqrt(10 ** (nrepeating + nfree + 1))) + 5
    s = set()
    for p in iterate_repeating(digit, nrepeating, nfree):
        if isprime(p, max_prime):
            s.add(p)
    return s


def mns(n, d):
    for i in range(n, 0, -1):
        s = get_primez_digit(d, i, n - i)
        if s:
            return i, len(s), sum(list(s))


def s(n):
    return sum((mns(n, d)[2] for d in range(10)))


print(s(10))
