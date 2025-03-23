s = open("day9_input.txt").read().strip()

v = []

empty = False
block_id = 0
for c in s:
    c = int(c)
    if c == 0:
        empty = not empty
        continue
    if empty:
        v += [None] * c
    else:
        v += [block_id] * c
        block_id += 1

    empty = not empty


def compress(v):
    idx = 0
    v = v[:]
    empty_count = sum(x is None for x in v) 

    while empty_count > 0:
        # pop one from the right
        while v[-1] is None:
            v.pop()
            empty_count -= 1
            if empty_count <= 0:
                return v
        move_block = v.pop()
        while v[idx] != None:
            idx += 1
        v[idx] = move_block
        empty_count -= 1
    return v

def score(v):
    return sum(v[i] * i for i in range(len(v)))

print(score(compress(v)))
