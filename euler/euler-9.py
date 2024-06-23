
#!/usr/bin/env python3

from functools import reduce
from operator import mul


def foo():
    for i in range(1, 1001):
        for j in range(1, 1001):
            a, b, c = sorted((i, j, 1000 - i - j))
            if a * a + b * b == c * c:
                return (a, b, c)


print(reduce(mul, foo()))
