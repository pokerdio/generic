def revD(a, b):
    """3x->x"""
    yield a * 3, b * 3


def revU(a, b):
    """3x+1->4x+2"""
    if a % 4 == 0:
        if b % 4 == 2:
            yield a // 4 * 3, b // 4 ** 3 + 1

    elif a % 4 == 2:
        if b % 4 == 2:  # x has to be even
            yield a // 2 * 3, b // 4 ** 3 + 1
        elif b % 4 == 0:  # x has to be odd
            yield a // 2 * 3, b // 4 * 3 + 1
    elif a % 2 == 1:
        for q in range(4):
            a1 = 4 * a
            b1 = (a * q) + b
            if b1 % 4 == 2:
                yield a1 // 4 * 3, b1 // 4 * 3 + 1


def revd(a, b):
    """3x+2->2x+1"""
    if a % 2 == 0:
        if b % 2 == 0:
            return
        else:
            yield a // 2 * 3, b // 2 * 3 + 2
    else:
        if b % 2 == 0:
            #            ->29x + 10
            #            x->2y + 1
            #            ->29 * 2y + 39
            yield a * 3, (b + a) // 2 * 3 + 2
        else:
            # ->29x + 7
            # x->2y
            # ->29*2y + 7
            yield a * 3, b // 2 * 3 + 2


def sequence(n, k=100):
    if n <= 1 or k <= 0:
        return ""
    if n % 3 == 0:
        return "D" + sequence(n // 3, k - 1)
    if n % 3 == 1:
        return "U" + sequence(n // 3 * 4 + 2, k - 1)
    if n % 3 == 2:
        return "d" + sequence(n // 3 * 2 + 1, k - 1)


def revert(seq, a=1, b=0, revs={"D": revD, "d": revd, "U": revU}):
    if not seq:
        yield a, b
        return

    for a1, b1 in revs[seq[-1]](a, b):
        yield from revert(seq[:-1], a1, b1)


def go(seq, minval):
    for a, b in revert(seq):
        if b > minval:
            yield b
        else:
            yield ((minval - b) // a + 1) * a + b


print(list(go("UDDDUdddDDUDDddDdDddDDUDDdUUDd", 10**15)))
