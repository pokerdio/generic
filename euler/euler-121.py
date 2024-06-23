def prize(n):
    blue = [1] * 2 + [0] * (n - 1)
    for i in range(1, n):
        newblue = [0] * (n + 1)

        for j in range(n + 1):
            newblue[j] = blue[j] * (i + 1)
        for j in range(1, n + 1):
            newblue[j] += blue[j - 1]

        blue = newblue

    wins = sum(blue[n // 2 + 1:])
    losses = sum(blue[:n // 2 + 1])
    return losses // wins + 1


print(prize(15))
