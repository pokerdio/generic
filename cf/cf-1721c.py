ntest = int(input())

def read_ints ():
    return list(int(x) for x in input().split())

d = [0] * 200050

for _ in range(ntest):
    n = int(input())
    a, b = (read_ints() for _ in "ab")

#min
    d[0] = b[0] - a[0]
    last = 0
    for i in range(1, n):
        while last < i and b[last] < a[i]:
            last += 1

        d[i] = b[last] - a[i]


    print (" ".join(str(d[x]) for x in range(n)))

# max     
    d[n - 1] = b[n - 1] - a[n - 1]
    last = n - 1 
    for i in range(n - 2, -1, -1):
        if b[i] < a[i + 1]:
            last = i
        d[i] = b[last] - a[i]
    print (" ".join(str(d[x]) for x in range(n)))
