def num2base(n, b):
    s = ""
    while n > 0:
        s = str(n % b) + "  " + s
        n //= b
    return s


def go(p, q, k):
    """the result must be given mod p**k"""

    ret = 0
    pk = p ** k

    x = 0
    digitz = yielddigitz(p, q, k)

    pepe = 1
    for _ in range(k):
        x = x + next(digitz) * pepe
        pepe *= p
    pk = p ** k
    while True:
        ret += x
        ret %= pk
        x //= p
        next_digit = next(digitz, None)
        if type(next_digit) == int:
            x += next_digit * p ** (k - 1)
        else:
            break
    return ret


def yielddigitz(p, q, k):
    s = 290797

    for i in range(q):
        s = s * s % 50515093
        yield s % p  # skippin the first digit
    for i in range(k + 5):
        yield 0
