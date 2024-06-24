import primez

from math import log
n = 800800
max_val = n * log(n)


pv = list(primez.iterate_primez(max_val * 1.5))

logpv = [log(x) for x in pv]
count = 0

last = 0
j = len(pv) - 1
for i in range(len(pv)):
    p = pv[i]
    while logpv[i] * pv[j] + logpv[j] * p > max_val:
        j -= 1
        if (j <= i):
            break

    if (j <= i):
        break
    count += (j - i)

print(count)
