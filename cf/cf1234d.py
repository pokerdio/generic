s = list(input())
m = int(input())


def make_st(s, seg_tree=None, idx=None, l=None, r=None):
    n = len(s)
    if seg_tree == None:
        seg_tree = [None for _ in range(n * 4)]
        idx = 0
        l = 0
        r = n
    if r - l == 1:
        seg_tree[idx] = {s[l]}
        return seg_tree
    mid = (l + r)//2
    idx2 = idx * 2 + 1
    make_st(s, seg_tree, idx2, l, mid)
    make_st(s, seg_tree, idx2+1, mid, r)
    seg_tree[idx] = seg_tree[idx2] | seg_tree[idx2+1]
    return seg_tree


def str_make(s, seg_tree, pos, c, idx=None, l=None, r=None):
    if idx == None:
        if s[pos] == c:
            return
        s[pos] = c
        idx = 0
        l = 0
        r = len(s)

    if l == pos and r == pos + 1:
        seg_tree[idx] = {c}
        return
    mid = (l + r) // 2
    idx2 = 2 * idx + 1
    if mid > pos:
        str_make(s, seg_tree, pos, c, idx2, l, mid)
    else:
        str_make(s, seg_tree, pos, c, idx2 + 1, mid, r)
    seg_tree[idx] = seg_tree[idx2] | seg_tree[idx2 + 1]


def str_chars(s, seg_tree, target_l, target_r, idx=None, l=None, r=None):
    if idx == None:
        idx = 0
        l = 0
        r = len(s)

    if target_l == l and target_r == r:
        return seg_tree[idx]
    mid = (l + r) // 2
    idx2 = idx * 2 + 1
    if target_r <= mid:
        return str_chars(s, seg_tree, target_l, target_r, idx2, l, mid)
    if target_l >= mid:
        return str_chars(s, seg_tree, target_l, target_r, idx2 + 1, mid, r)

    sl = str_chars(s, seg_tree, target_l, mid, idx2, l, mid)
    sr = str_chars(s, seg_tree, mid, target_r, idx2+1, mid, r)
    return sl | sr


st = make_st(s)

for m in range(m):
    typ, a, b = input().split()
    if typ == "1":
        str_make(s, st, int(a) - 1, b)
    if typ == "2":
        a, b = int(a), int(b)
        if a == b:
            print(1)
        else:
            print(len(str_chars(s, st, int(a)-1, int(b))))
