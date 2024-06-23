def foo():
    v = {(0, 0): 1}

    for i in range(1, 101):
        i2 = i * i

        print(i, len(v))

        if i > 51:
            d = [(s, k) for (s, k), v in v.items() if k < i - 51]
            for key in d:
                del v[key]

        v2 = v.copy()

        for (s, k), variants in v.items():
            if k < 50:
                key = (s + i2, k + 1)
                v2[key] = v2.get(key, 0) + variants
        v = v2

        # if i == 3:
        #     print(v)
        #     return
    ret = 0
    for (s, k), variants in v.items():
        if variants == 1 and k == 50:
            ret += s
    return ret
