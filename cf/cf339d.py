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


n, m = (pop_int() for _ in range(2))
n2 = 2 ** n
a = [pop_int() for _ in range(n2)]

queries = [(pop_int(), pop_int()) for _ in range(m)]


"""we maek segment tree then defense it"""


def make_st(a, l=None, r=None, idx=0, is_xor=None, v=None):
    if is_xor == None:
        l = 0
        r = n = len(a)
        v = [0] * (r - 1)
        while n >= 1:
            is_xor = not is_xor
            n //= 2
    n = len(a)
    if r - l == 2:
        assert not is_xor
        v[idx] = a[l] | a[l + 1]
        return v

    mid = (l + r) // 2
    idx_l, idx_r = idx * 2 + 1, idx * 2 + 2
    make_st(a, l, mid, idx_l, not is_xor, v)
    make_st(a, mid, r, idx_r, not is_xor, v)
    if is_xor:
        v[idx] = v[idx_l] ^ v[idx_r]
    else:
        v[idx] = v[idx_l] | v[idx_r]
    return v


def query(a, v, p, b, idx=None, l=None, r=None, is_xor=None):
    if is_xor == None:
        l = 0
        r = n = len(a)
        idx = 0
        while n > 0:
            n //= 2
            is_xor = not is_xor

    if r - l == 2:
        assert not is_xor
        a[p] = b
        v[idx] = b | a[l + (p == l)]
        return v[idx]
    mid = (l + r) // 2
    idx_l = idx * 2 + 1
    idx_r = idx_l + 1
    if p < mid:
        query(a, v, p, b, idx_l, l, mid, not is_xor)
    if p >= mid:
        query(a, v, p, b, idx_r, mid, r, not is_xor)
    val_l = v[idx_l]
    val_r = v[idx_r]
    if is_xor:
        v[idx] = val_l ^ val_r
    else:
        v[idx] = val_l | val_r
    return v[idx]


v = make_st(a)

for p, b in queries:
    print(query(a, v, p - 1, b))
