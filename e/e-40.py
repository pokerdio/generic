#!/usr/bin/env python3

# https://projecteuler.net/problem=38
#
import math
from operator import mul

from functools import reduce


s = "".join((str(x) for x in range(1, 250000)))


print(reduce(mul, (int(s[10 ** x - 1]) for x in range(7))))
