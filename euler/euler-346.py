def go(n):
    g = set((1,))
    for i in range(2, int(sqrt(n)) + 1):
        k = 1 + i + i * i
        while k <= n:
            g[k] = g.get(k, 0) + 1
            k = k * i + 1
    return sum(i for i in g.keys())
