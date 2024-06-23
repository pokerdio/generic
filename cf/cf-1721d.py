def read_int():
    return int(input())

ntest = read_int()

def read_ints ():
    return list(int(x) for x in input().split())


def vibes(va, vb, bit):
    """whether it is possible to get a one in the one active bit in the bitmask 
in the and of the xors of va and permutated vb"""

    n = len(va)
    assert(len(vb) == n)
    ka, kb = 0, 0 # number of hits on the bit in the bitmask in the vectors

    for i in range(n):
        if va[i] & bit:
            ka += 1
        if vb[i] & bit:
            kb += 1
    
    if ka + kb == n:
        return 1, (ka and kb)
    return 0, 0

def split(va, vb, bit):
    va1, va2 = [], []
    vb1, vb2 = [], []
    va1 = [x for x in va if x & bit]
    va2 = [x for x in va if not (x&bit)]
    vb1 = [x for x in vb if not (x & bit)]
    vb2 = [x for x in vb if x & bit]
    assert(len(va1) == len(vb1))
    assert(len(va2) == len(vb2))

    return va1, vb1, va2, vb2

for _ in range(ntest):
    n = read_int()
    a, b = ([read_ints()] for _ in "ab")

    ret = 0
    for twopow in range(29, -1, -1):
        bitmask = 2 ** twopow

        okay = True
        must_split = [0] * len(a)
        for i in range(len(a)):
            vibe, must_split[i] = vibes(a[i], b[i], bitmask)
            if not vibe:
                okay = False
                break
        if okay:
            a2 = []
            b2 = []
            
            if twopow > 0:
                for i in range(len(a)):
                    if must_split[i]:
                        aa1, bb1, aa2, bb2 = split(a[i], b[i], bitmask)
                        a2.append(aa1)
                        b2.append(bb1)
                        a2.append(aa2)
                        b2.append(bb2)
                    else:
                        a2.append(a[i])
                        b2.append(b[i])
            ret += bitmask
            a = a2
            b = b2
    print(ret)
    
