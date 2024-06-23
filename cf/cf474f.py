from math import gcd
import sys

input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


def pop_str():
    global input_str_idx
    input_str_idx += 1
    return input_str[input_str_idx - 1]


n = pop_int()
s = [pop_int() for _ in range(n)]
t = pop_int()

query = [(pop_int(), pop_int()) for _ in range(t)]


def make_segtree(s, st=None, idx=None, l=None, r=None):
    """segment tree tracking gcd, min value, min value count of segments"""
    if st == None:
        l = 0
        r = len(s)
        st = [None] * (4 * r)
        idx = 0

    if l + 1 == r:
        st[idx] = (s[l], s[l], 1)
        return st
    mid = (l + r) // 2
    idx_l = 2 * idx + 1
    idx_r = idx_l + 1
    make_segtree(s, st, idx_l, l, mid)
    make_segtree(s, st, idx_r, mid, r)
    gcd1, min1, count1 = st[idx_l]
    gcd2, min2, count2 = st[idx_r]
    count12 = count1 + count2 if min1 == min2 else min(((min1, count1), (min2, count2)))[1]
    st[idx] = (gcd(gcd1, gcd2), min(min1, min2), count12)
    return st


def query_segtree(st, target_l, target_r, idx=None, l=None, r=None):
    if idx == None:
        idx = l = 0
        r = len(st) // 4
    if l == target_l and r == target_r:
        return st[idx]
    mid = (l + r) // 2
    idx_l = idx * 2 + 1
    idx_r = idx_l + 1
    if target_r <= mid:
        return query_segtree(st, target_l, target_r, idx_l, l, mid)

    if target_l >= mid:
        return query_segtree(st, target_l, target_r, idx_r, mid, r)

    gcd1, min1, count1 = query_segtree(st, target_l, mid, idx_l, l, mid)
    gcd2, min2, count2 = query_segtree(st, mid, target_r, idx_r, mid, r)
    count12 = count1 + count2 if min1 == min2 else min(((min1, count1), (min2, count2)))[1]
    return (gcd(gcd1, gcd2), min(min1, min2), count12)


st = make_segtree(s)

for l, r in query:
    l = l - 1
    gcd_seg, min_seg, count_min_seg = query_segtree(st, l, r)
    n = r - l
    if gcd_seg % min_seg == 0:
        print(n - count_min_seg)
    else:
        print(n)
