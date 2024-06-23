n = int(input())
ones = [tuple(int(s) for s in input().split()) for _ in range(n - 1)]

m = [[0] * n for _ in range(n)]

col_sum = [0] * n
for row, column in ones:
    m[row - 1][column - 1] = 1
    col_sum[column - 1] += 1

row_sum = [sum(row) for row in m]


ret = []

for i in range(n - 1):
    col = max(range(i, n), key=lambda col: col_sum[col])
    if col_sum[col] == 0:
        break  # job done all remaining columns are empty
    if col != i:
        # swapping columns
        ret.append((2, i, col))
        col_sum[i], col_sum[col] = col_sum[col], col_sum[i]
        for j in range(n):
            m[j][i], m[j][col] = m[j][col], m[j][i]

    if row_sum[i] > 0:
        for j in range(i + 1, n):
            if row_sum[j] == 0:
                # swapping lines
                ret.append((1, i, j))
                m[i], m[j] = m[j], m[i]
                row_sum[i], row_sum[j] = row_sum[j], row_sum[i]
                break
    # adjusting the row sums to exclude the ith column
    for j in range(n):
        if m[j][i]:
            row_sum[j] -= 1


print(len(ret))
for a, b, c in ret:
    print("%d %d %d" % (a, b + 1, c + 1))
