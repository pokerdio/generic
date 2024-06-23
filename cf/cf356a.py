import sys

input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


n, m = pop_int(), pop_int()
lrx = [(pop_int(), pop_int(), pop_int()) for _ in range(m)]


def make_st(n):
    active = [0] * (4*n)
    active[0] = 1
    return [0] * (4 * n), active


def paint_st(n, v, active, targetl, targetr, x, idx=None, l=None, r=None):
    if idx == None:
        idx = 0
        l = 0
        r = n

    #print(f"painting target: {targetl}-{targetr} <- {x} - idx{idx}:{l}-{r}")
    if targetl == l and targetr == r:
        v[idx] = x
        active[idx] = 1
        return

    idx_l = idx * 2 + 1
    idx_r = idx_l + 1
    if active[idx]:
        active[idx] = 0
        active[idx_l] = 1
        active[idx_r] = 1
        v[idx_l] = v[idx]
        v[idx_r] = v[idx]
    mid = (l + r) // 2
    if targetr <= mid:
        paint_st(n, v, active, targetl, targetr, x, idx_l, l, mid)
    elif targetl >= mid:
        paint_st(n, v, active, targetl, targetr, x, idx_r, mid, r)
    else:
        paint_st(n, v, active, targetl, mid, x, idx_l, l, mid)
        paint_st(n, v, active, mid, targetr, x, idx_r, mid, r)


def st_repr(n, v, idx=None, l=None, r=None):
    if idx == None:
        idx = 0
        l = 0
        r = n
    if active[idx]:
        val = v[idx]
        return " ".join(str(val) for i in range(l, r))
    else:
        mid = (l + r) // 2
        strl = st_repr(n, v, idx * 2 + 1, l, mid)
        strr = st_repr(n, v, idx * 2 + 2, mid, r)
        return strl + " " + strr


v, active = make_st(n)
for l, r, x in reversed(lrx):
    if x == r:
        paint_st(n, v, active, l - 1, r-1, x)
    elif x == l:
        paint_st(n, v, active, l, r, x)
    else:
        paint_st(n, v, active, l - 1, x - 1, x)
        paint_st(n, v, active, x, r, x)

print(st_repr(n, v))
