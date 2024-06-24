import heapq
from math import sqrt


def bar(n=10**6):
    ret = 0
    sieve = list(range(n + 2))
    for i in range(2, n + 2):
        if sieve[i] == i:
            for j in range(i, n + 1, i):
                sieve[j] = i  # biggest prime that divides j is i
        if max(sieve[i], sieve[i - 1]) <= 47:
            #            print(i - 1, sieve[i - 1], sieve[i])
            ret += i - 1
    return ret


def bar2(n=10**6):
    ret = []
    sieve = list(range(n + 2))
    for i in range(2, n + 2):
        if sieve[i] == i:
            for j in range(i, n + 1, i):
                sieve[j] = i  # biggest prime that divides j is i
        if max(sieve[i], sieve[i - 1]) <= 47:
            #            print(i - 1, sieve[i - 1], sieve[i])
            ret.append(i - 1)
    return ret


def listp(n):
    sieve = list(range(n + 2))
    ret = []
    for i in range(2, n + 1):
        if sieve[i] == i:
            ret.append(i)
            for j in range(i, n + 1, i):
                sieve[j] = i
    return ret


def smooth_frends(v):
    ret = 0
    for i in range(len(v) - 1):
        if v[i+1]-v[i] == 1:
            ret += v[i]
    return ret


def smooth_frends_lst(v):
    ret = []
    for i in range(len(v) - 1):
        if v[i+1]-v[i] == 1:
            ret.append(v[i])
    return ret


def gen_smooth(n, p=47):
    pv = listp(p)
    v = [1]

    for p in pv:
        new = []
        i = p
        while i <= n:
            for j in v:
                if j * i <= n:
                    new.append(j * i)
                else:
                    break
            i *= p
        v.extend(new)
        v.sort()
    return v


def foo(n):
    return smooth_frends_lst(gen_smooth(n + 1))


def foo2(n):
    return smooth_frends(gen_smooth(n + 1))


print(foo2(10**14))


# solution to problem 204:
#print(len(gen_smooth(10**9, 97)))
