def readints():
    return [int(x) for x in input().split(" ")]


m, n = readints()
print(m * n // 2)
