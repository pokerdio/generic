from builtins import sum
from itertools import combinations

# assuming the significant digits are more than the longest
# nonzero digitz 9111 111 111


def gen_sums(total, max=9):
    if max > total:
        max = total
    for i in range(1, max + 1):
        if i == total:
            yield (total,)
        else:
            for s in gen_sums(total - i, i):
                yield (i, *s)


def gen_perm_sums(total, remain, master):
    if master:
        if remain:
            for s in gen_perm_sums(total, remain, False):
                yield((total, *s))
        else:
            yield(total,)
    for i in range(1, remain):
        for s in gen_perm_sums(total, remain - i, master):
            yield((i, *s))
    if master:
        if total > remain:
            yield (remain, total)
    else:
        yield((remain,))


def gen_sig_nums(sign, sig_digitz):
    for p in combinations(range(sig_digitz), len(sign)):
        ret = 0
        for i in range(len(sign)):
            ret += sign[i] * 10 ** p[i]
        yield ret


def go_sig(signature, total_digitz, sig_digitz=16):

    mod = 10 ** sig_digitz  # significant digitz

    ret = 0
    for i in range(len(signature)):
        iret = 0
        for num in gen_sig_nums(signature[i:], sig_digitz):
            iret += num
        ret = (ret + iret * zero_count(i, total_digitz - sig_digitz)) % mod
    return ret % mod


def go(total_digitz, sig_digitz):
    ret = 0
    mod = 10 ** sig_digitz
    for i in range(1, 10):  # max digit, sum of others
        print("i", i)
        for sign in gen_perm_sums(i, i, True):
            print("signature", sign)
            ret += go_sig(sign, total_digitz, sig_digitz)
    return ret % mod


def zero_count(n, m, mod=10**16):
    """counts ways a nonzero number of n digits 
    is brought to up to m digitz by internal zeros"""

    if n == 0:
        return 1

    # simply out of the m digit places, we pick spots for our n digits
    # this takes care of trailing zeros too
    return comb(m, n, mod)


def fact(n, data={0: 1, 1: 1}):
    if n in data:
        return data[n]
    else:
        f = 1
        for i in range(2, n + 1):
            f = f * i
            data[i] = f
        return data[n]


fact(2020)


def comb(n, k, mod=10**16, data={}):
    # don't call with different mods at different times plzkthx
    nk = (n, k)
    assert(n >= k)
    if nk in data:
        return data[nk]
    else:
        ret = (fact(n) // fact(k) // fact(n - k)) % mod
        data[nk] = ret
        return ret


#go(2020, 16)
