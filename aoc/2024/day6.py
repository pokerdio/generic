v = [list(s.strip()) for s in open("day6_input.txt").readlines()]


dir = ((0, -1), (1, 0), (0, 1), (-1, 0))
dir_idx = 0

for i in range(len(v)):
    for j in range(len(v[0])):
        if v[i][j] == "^":
            x = j
            y = i

ret = 0

done = False
while True:
    for i in range(4):
        x1, y1 = x + dir[(dir_idx + i) % 4][0], y + dir[(dir_idx + i) % 4][1]
        if x1 < 0 or x1 >= len(v[0]) or y1 < 0 or y1 >= len(v):
            done = True
            break
        if (v[y1][x1] != "#"):
            v[y1][x1] = "^"
            x, y = x1, y1
            dir_idx = (dir_idx + i) % 4
            break

    if done:
        print(sum("".join(s).count("^") for s in v))
        break
        

    
