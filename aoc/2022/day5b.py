lines = [s.rstrip() for s in open("day5_input.txt").readlines()]

import re

v = [[] for _ in range(10)]

first_phase = True

pat = re.compile(r"move ([0-9]+) from ([0-9]) to ([0-9])")

for s in lines:
    if first_phase:
        if (re.search(r"[0-9]", s)):
            first_phase = False

        for i in range(1, 10):
            j = (i - 1) * 4 + 1
            if (j < len(s) and s[j] >= "A" and s[j] <= "Z"):
                v[i].insert(0, s[j])
    else:
        m = pat.match(s)
        if (m): 
            count = int(m[1])
            src = int(m[2])
            dest = int(m[3])
            v[dest] += v[src][-count:]
            v[src] = v[src][:-count]

s = ""
for i in range(1, 10):
    s += v[i].pop()

print(s)
