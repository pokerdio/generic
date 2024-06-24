#!/usr/bin/env python3



from fractions import Fraction as Fr
from itertools import permutations as perm
from itertools import count, product


def natural(fr):
    if fr.denominator == 1 and fr.numerator > 0:
        return fr.numerator


def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def times(a, b):
    return a * b


def divide(a, b):
    return a / b


ops = [plus, minus, times, divide]


def results_set(digits):
    # digits is a set of fractions, each a digit number
    rez = set()
    for op1, op2, op3 in product(ops, repeat=3):
        for d in perm(digits):
            try:
                value = op1(op2(op3(d[0], d[1]), d[2]), d[3])
                if natural(value):
                    rez.add(int(value))
            except:
                print("(%s (%s (%s %d %d) %d) %d)" %
                      ((op1.__name__, op2.__name__, op3.__name__,
                        int(d[0]), int(d[1]), int(d[2]), int(d[3]))))
            try:
                value = op1(op2(d[0], d[1]), op3(d[2], d[3]))
                if natural(value):
                    rez.add(int(value))
            except:
                print("(%s (%s %d %d) (%s %d %d))" %
                      ((op1.__name__, op2.__name__, int(d[0]), int(d[1]),
                        op3.__name__, int(d[2]), int(d[3]))))

    return rez


def topn(setvalue):
    for i in count(1):
        if i not in setvalue:
            break
    return i - 1


def go():
    bestscore = -1
    best = None

    digi_strings = set(("".join(sorted(s)) for s in
                        (str(i) for i in range(1000, 10000))
                        if (len(set(s)) == 4) and "0" not in s))

    for s in digi_strings:
        digits = [Fr(x) for x in s]
        score = topn(results_set(digits))
        if score > bestscore:
            bestscore = score
            best = str(sorted(digits))
    return best
