n = int(input())
d = {"X++": 1, "X--": -1, "++X": 1, "--X": -1}


print(sum(d[input()] for _ in range(n)))
