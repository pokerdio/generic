n, k = [int(x) for x in input().split(" ")]
if n == k:
    print(86400)
    exit()

tm, dur = list(zip(*((int(x) for x in (input().split(" "))) for _ in range(n))))


best = tm[k] - 1
besttxt = "initial"
v = [0] * (k + 1)
v2 = v.copy()

last_t = 0
for i in range(n):
    dt = tm[i] - last_t
    last_t = tm[i]
    idur = dur[i]

    irest = n - i - 1
#    print(f"idur{idur} irest {irest}")
    for skips, val in enumerate(v):  # skips <- used up skips
        v2[skips] = max(val - dt, 0) + idur

        oldbest = best
        if irest <= k - skips:  # sleep rest of day:
            best = max(best, 86401 - v2[skips] - last_t)
            if best > oldbest:
                besttxt = f"start at {i} having skipped {skips} up to the end"
#                print("new best", besttxt)
        else:
            best = max(best, tm[i + 1 + k - skips] - v2[skips] - last_t)
            if best > oldbest:
                besttxt = f"start at {i} having skipped {skips} up to {i + 1+ k - skips}"
#                print("new best2", besttxt)

        if skips > 0:
            v2[skips] = min(v2[skips], max(v[skips - 1] - dt, 0))

    v, v2 = v2, v
#    print(f"loop {i} ends v={v} ")
print(best)  # , besttxt)
