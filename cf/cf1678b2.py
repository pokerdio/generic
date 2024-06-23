import sys
t = int(input())


for _ in range(t):
    n = int(input())
    s = sys.stdin.readline()

    #print("test ", n, s)

    change_count = 0
    seg_count_zero = 1
    seg_count_one = 1
    for xx in [s[i:i+2] for i in range(0, n, 2)]:
        if xx == "00":
            seg_count_zero = min(seg_count_zero, seg_count_one + 1)
            seg_count_one = 999999
        elif xx == "11":
            seg_count_one = min(seg_count_one, seg_count_zero + 1)
            seg_count_zero = 999999
        elif xx == "01" or xx == "10":
            change_count += 1
            z1 = min(seg_count_zero, seg_count_one + 1)
            o1 = min(seg_count_one, seg_count_zero + 1)
            seg_count_zero, seg_count_one = z1, o1

        #print("after", xx, change_count, " 0:", seg_count_zero, " 1:", seg_count_one)

    print(change_count, min(seg_count_zero, seg_count_one))
