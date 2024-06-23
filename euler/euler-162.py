from functools import reduce


def prod(v):
    return reduce((lambda x, y: x * y), v)


s = 0

for length in range(3, 17):
    v = [16] * length
    assert(len(v) == length)
    for zero in range(1, length):
        for A in range(length):
            if A != zero:
                for one in range(length):
                    if A != one and one != zero:
                        v2 = v[:]
                        for i in sorted((A, one, zero)):
                            for j in range(i):
                                v2[j] -= 1
                        for i in (A, one, zero):
                            v2[i] = 1
                        s += prod(v2)


print(hex(s).upper())
