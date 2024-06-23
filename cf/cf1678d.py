import sys
t = int(input())


for _ in range(t):
    n, m = (int(c) for c in input().split())
    s = sys.stdin.readline()

    v = []
    last_good = -10000010
    columns = set()
    ret = []
    for i in range(n * m):
        igood = (s[i] == "1")

        if igood:
            last_good = i
            columns.add(i % m)

        if i >= m:
            last_line_count = v[i - m]
        else:
            last_line_count = 0

        v.append(last_line_count + (last_good > i - m))

        ret.append(len(columns) + v[-1])
    print(" ".join(map(str, ret)))
