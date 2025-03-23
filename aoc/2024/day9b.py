s = open("day9_input.txt").read().strip()

v = []

empty = False
block = []

for c in s:
    c = int(c)
    if c == 0:
        empty = not empty
        continue
    if empty:
        v += [None] * c
    else:
        block.append((len(v), len(v) + c))
        v += [len(block) - 1] * c

    empty = not empty

def findEmpty(v, block_start, block_end, start_size):
    cur_size = 0
    size = block_end - block_start
    for i in range(start_size[size], block_start):
        if v[i] == None:
            cur_size += 1
        else:
            cur_size = 0
        if cur_size == size:
            for j in range(size):
                v[i - size + 1 + j] = v[block_start + j]
                v[block_start + j] = None
            for j in range(size, 10):
                start_size[j] = i + 1
            return
    for j in range(size, 10):
        start_size[j] = block_start


def compress(v, block):
    start_size = [0] * 10 # where to start looking for blocks of various sizes
    # to not start from 0 every time

    for idx in range(len(block)-1, -1, -1):
        findEmpty(v, *block[idx], start_size = start_size)


compress(v, block)

def score(v):
    return sum(v[i] * i for i in range(len(v)) if v[i] != None)

print(score(v))
