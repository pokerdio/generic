n, t = (int(x) for x in input().split())
queue = input()

for i in range(t):
    queue = queue.replace("BG", "GB")

print(queue)
