v = {(i, i, i): 1 for i in range(10)}


def step():
    global v
    v2 = {}

    for packed, count in v.items():
        last_digit, min_digit, max_digit = packed
        if last_digit > 0:
            new = (last_digit - 1, min(min_digit, last_digit - 1), max_digit)
            v2[new] = v2.get(new, 0) + count

        if last_digit < 9:
            new = (last_digit + 1, min_digit, max(max_digit, last_digit + 1))
            v2[new] = v2.get(new, 0) + count
    v = v2


s = 0
for i in range(39):
    step()
    s += sum(v.get((i, 0, 9), 0) for i in range(1, 10))


print(s)
