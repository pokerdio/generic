from itertools import product

n = int(input())
a = [int(x) + 1 for x in input().split(" ")]

#n = 2
#a = [2, 3]


nstate = 1
for x in a:
    nstate *= x

win = bytearray(nstate)


delta = [1]
for i in range(1, n):
    delta.append(delta[-1] * a[i - 1])
deltasum = sum(delta)

b = [0, 0, 0]

for state in range(1, nstate):
    i = 0
    b[0] += 1
    while b[i] >= a[i]:
        b[i] = 0
        i += 1
        b[i] += 1
    try:
        for i, d in enumerate(delta):
            for x in range(d, (b[i] + 1) * d, d):
                if not win[state - x]:
                    win[state] = 1
                    raise Exception()
        for x in range(deltasum, (min(b[:n]) + 1) * deltasum, deltasum):
            if not win[state - x]:
                win[state] = 1
                raise Exception()
    except Exception:
        pass


print(win[-1] and "BitLGM" or "BitAryo")
