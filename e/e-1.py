#!/usr/bin/env python3


#print(sum(set(range(3, 1000, 3)) | set(range(5, 1000, 5))))


def foo(v, r, ve, re, drf=0.644):
    return min(1.0, r / re, (r * ve / (re * v)) ** drf)


def optimalspeed(r, ve, re, drf=0.644):
    ret = 0
    for v in range(1, 15000):
        if foo(v, r, ve, re, drf) > (min(r / re, 1.0) * 0.99):
            ret = v
    return ret
