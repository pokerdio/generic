t = int(input())

for _ in range(t):
    n = int(input())
    ca = list(int(c) for c in input().split())
    cb = list(int(c) for c in input().split())
    cola = [0] * (n + 1)  # position the index color is found in tape "ca"
    for i in range(n):
        cola[ca[i]] = i
    #print(f"test {_} {n} {ca} {cb} {cola}")

    vis = [0] * n

    ret = 0
    mid = (n - 1.0) / 2.0

    min = +mid
    max = +mid

    for i in range(n):
        if not vis[i]:
            k = 0
            #print(f"cycle starting at {i}")
            while not vis[i]:
                vis[i] = 1
                i = cola[cb[i]]
                #print(f"goes to {i}")
                k += 1
            for j in range(k // 2):
                ret += 2 * max + 2 * min
                max -= 1.0
                min -= 1.0
    print(int(ret))
