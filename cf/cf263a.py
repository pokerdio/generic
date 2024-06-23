v = [[int(c) for c in input().split(" ")] for _ in range(5)]


one_line = [sum(line) for line in v].index(1)
one_column = v[one_line].index(1)
half = len(v) // 2
print(abs(one_line - half) + abs(one_column - half))
