import sys
input_str = sys.stdin.read().split()
input_str_idx = 0


def pop_int():
    global input_str_idx
    input_str_idx += 1
    return int(input_str[input_str_idx - 1])


n = pop_int()
vx, vy = zip(*[(pop_int(), pop_int()) for _ in range(n)])
maxfriend = [0] * n

for i in range(n):
    for j in range(i - vy[i], i):
        maxfriend[j] = i

m = max(vx)
#print(m, str(friends))
div = [0] * n

for d in range(2, m + 1):
    plus, minus = [0] * n, [0] * n
    for i, x in enumerate(vx):
        if x % d == 0:
            plus[i] = 1
            for j in range(i + 1, maxfriend[i] + 1):
                if j - i <= vy[j] and vx[j] % d == 0:
                    minus[j] = 1
    for i in range(n):
        div[i] += plus[i] - minus[i]

for i in range(n):
    print(div[i] + (not vy[i]))
