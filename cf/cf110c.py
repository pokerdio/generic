n = int(input())

for i in range(10):
    if (n >= 4 * i and (n - 4 * i) % 7 == 0):
        print("4" * i + "7" * ((n - 4 * i) // 7))
        break
else:
    print(-1)
