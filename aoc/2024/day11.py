v = {int(word):1 for word in open("day11_input.txt").read().strip().split()}



def blink(v):
    ret = {}
    for x, count in v.items():
        if x == 0:
            ret[1] = ret.get(1, 0) + count
        elif len(str(x)) % 2 == 0:
            s = str(x)
            n = len(s)
            first = int(s[:n // 2])
            second = int(s[n // 2:])
            ret[first] = ret.get(first, 0) + count
            ret[second] = ret.get(second, 0) + count
        else:
            x2024 = x * 2024
            ret[x2024] = ret.get(x2024, 0) + count
    return ret



def problim(v, n):
    for t in range(n):
        v = blink(v)
    return v

print(sum(problim(v, 25).values()))
print(sum(problim(v, 75).values()))

