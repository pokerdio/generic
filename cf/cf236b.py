a, b, c = (int(x) for x in input().split())
#a, b, c = 5, 6, 7


div = [0] * 101

for i in range(2, 101):
    if div[i] == 0:
        for j in range(2 * i, 101, i):
            div[j] = i


primez = list(x for x in range(2, 101) if not div[x])


def dict_add(d1, d2):
    for key, val in d2.items():
        if key in d1:
            d1[key] += val
        else:
            d1[key] = val
    return d1


decomp = [{}, {}]

for i in range(2, 101):
    if div[i] == 0:
        decomp.append({i: 1})
    else:
        decomp.append(dict_add({div[i]: 1}, decomp[i // div[i]]))

ret = 0

for i in range(1, a + 1):
    for j in range(1, b + 1):
        d = decomp[i].copy()
        dict_add(d, decomp[j])
        for k in range(1, c + 1):
            d2 = d.copy()
            dict_add(d2, decomp[k])
            tmp = 1
            for p, count in d2.items():
                tmp *= count + 1
            ret += tmp
        ret %= 1073741824
print(ret)
