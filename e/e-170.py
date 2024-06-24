count = 0


def go(i, j, k, ijset):
    global count
    count += 1

    if count < 50:
        print(i, j, k)


for i in range(2, 100000):
    istr = str(i)
    idigits = len(istr)

    if len(istr) > len(set(istr)):
        continue
    for j in range(1, 10**((10 - idigits) // 2)):
        jstr = str(j)
        jdigits = len(jstr)

        ijset = set(istr + jstr)
        if len(ijset) < idigits + jdigits:
            continue

        k = i * j
        kstr = str(k)
        if len(kstr) > len(set(kstr)):
            continue

        go(i, j, k, ijset)
