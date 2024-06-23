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


n, m = pop_int(), pop_int()
a = [pop_int() for _ in range(n)]

requests = [(pop_str(), pop_int(), pop_int(), pop_int()) for _ in range(m)]


def make_st_go(a, v, x, l, r, f):
    if l + 1 == r:
        v[x] = a[l]
    else:
        mid = (l + r) // 2
        make_st_go(a, v, x * 2 + 1, l, mid, f)
        make_st_go(a, v, x * 2 + 2, mid, r, f)
        v[x] = f(v[x * 2 + 1], v[x*2 + 2])


def sum(a, b):
    return (a + b) % 1000000007


def make_st(a, f):
    n = len(a)
    v = [0] * (n * 4 + 1)
    make_st_go(a, v, 0, 0, n, f)
    return v


def set_range(idx, a, v, ones, set_to, set_active, l, r, target_l, target_r, val):
    # print("set_range", idx, "-", l, r, "-", target_l, target_r, l == target_l and r == target_r)
    if l == target_l and r == target_r:
        for k in range(6):
            if r - l > 1:
                set_to[k][idx] = val
                set_active[k][idx] = True
            v[k][idx] = (val * ones[k][idx]) % 1000000007
        return
    assert r - l >= 2

    mid = (l + r) // 2
    idx_l = idx * 2 + 1
    idx_r = idx_l + 1

    for k in range(6):
        if set_active[k][idx]:
            set_active[k][idx] = False
            set_active[k][idx_l] = True
            set_active[k][idx_r] = True
            set_val = set_to[k][idx]
            set_to[k][idx_l] = set_val
            set_to[k][idx_r] = set_val
            v[k][idx_l] = (ones[k][idx_l] * set_val) % 1000000007
            v[k][idx_r] = (ones[k][idx_r] * set_val) % 1000000007

    if target_r <= mid:
        set_range(idx_l, a, v, ones, set_to, set_active, l, mid, target_l, target_r, val)
    elif target_l >= mid:
        set_range(idx_r, a, v, ones, set_to, set_active, mid, r, target_l, target_r, val)
    else:
        set_range(idx_l, a, v, ones, set_to, set_active, l, mid, target_l, mid, val)
        set_range(idx_r, a, v, ones, set_to, set_active, mid, r, mid, target_r, val)
    for k in range(6):
        v[k][idx] = sum(v[k][idx_l], v[k][idx_r])


def query_sum(idx, v, ones, set_to, set_active, l, r, target_l, target_r):
    idx_l = idx * 2 + 1
    idx_r = idx_l + 1
    if target_l == l and target_r == r:
        return v[idx]
    mid = (l + r) // 2

    if set_active[idx]:
        set_active[idx] = False
        set_active[idx_l] = True
        v[idx_l] = (ones[idx_l] * set_to[idx]) % 1000000007
        set_to[idx_l] = set_to[idx]
        set_active[idx_r] = True
        v[idx_r] = (ones[idx_r] * set_to[idx]) % 1000000007
        set_to[idx_r] = set_to[idx]

    if target_r <= mid:
        return query_sum(idx_l, v, ones, set_to, set_active, l, mid, target_l, target_r)
    if target_l >= mid:
        return query_sum(idx_r, v, ones, set_to, set_active, mid, r, target_l, target_r)

    val_l = query_sum(idx_l, v, ones, set_to, set_active, l, mid, target_l, mid)
    val_r = query_sum(idx_r, v, ones, set_to, set_active, mid, r, mid, target_r)
    return sum(val_l, val_r)


def go(a, req):
    n = len(a)
    v = [make_st([(a[i] * (i+1)**k) % 1000000007 for i in range(n)], sum) for k in range(6)]
    ones = [make_st([(i+1)**k % 1000000007 for i in range(n)], sum) for k in range(6)]
    set_to = [[0] * len(v[0]) for _ in range(6)]
    set_active = [[False] * len(v[0]) for _ in range(6)]

    for com, l, r, x in req:
        def query(x):
            return query_sum(0, v[x], ones[x], set_to[x], set_active[x], 0, n, l-1, r)

        if com == "=":
            set_range(0, a, v, ones, set_to, set_active, 0, n, l-1, r, x)
            # print(v[0])
            # print([i for i in range(len(set_active[0])) if set_active[0][i]])
            # return v[0], set_to[0], set_active[0]
        if com == "?":
            a0 = query(0)
            d = l - 1
            if x == 0:
                print(a0)
                continue
            a1 = query(1)
            if x == 1:
                print((a1 - a0 * d) % 1000000007)
                continue
            a2 = query(2)
            d2 = (d * d) % 1000000007
            if x == 2:
                print((a2 - 2 * d * a1 + d2 * a0) % 1000000007)
                continue
            a3 = query(3)
            d3 = (d ** 3) % 1000000007
            if x == 3:
                print((a3 - 3 * d * a2 + 3 * d2 * a1 - d3 * a0) % 1000000007)
                continue
            a4 = query(4)
            d4 = (d ** 4) % 1000000007
            if x == 4:
                print((a4 - 4 * d * a3 + 6 * d2 * a2 - 4 * d3 * a1 + d4 * a0) % 1000000007)
                continue
            a5 = query(5)
            d5 = (d ** 5) % 1000000007
            assert x == 5
            print((a5 - 5 * d * a4 + 10 * d2 * a3 - 10 * d3 * a2 + 5 * d4 * a1 - d5 * a0) % 1000000007)


go(a, requests)


def print_tree_go(idx, n, l, r, prefix):
    if l + 1 == r:
        print(f"{prefix}{idx}:{l+1}")
    else:
        print(f"{prefix}{idx}:{l+1}-{r}")
        mid = (l + r) // 2
        print_tree_go(idx * 2 + 1, n, l, mid, prefix + "  ")
        print_tree_go(idx * 2 + 2, n, mid, r, prefix + "  ")


def print_tree(n):
    print_tree_go(0, n, 0, n, "")
