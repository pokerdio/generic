def dice(faces, dicecount):
    maxface = max(faces)
    v = [1] + [0] * (dicecount * max(faces))

    for i in range(dicecount):
        v2 = [0] * len(v)
        for j in range(len(v) - maxface):
            for face in faces:
                v2[j + face] += v[j]
        v = v2
    return v


def sortadd(tupl, value):
    for i in range(len(tupl)):
        if value < tupl[i]:
            return tupl[:i] + (value,) + tupl[i:]
    return tupl + (value,)


def step(v, faces, maxtoplen):
    v2 = {}

    for top, count in v.items():
        for f in faces:
            newtop = sortadd(top, f)
            if len(newtop) > maxtoplen:
                newtop = newtop[1:]
            v2[newtop] = v2.get(newtop, 0) + count

    return v2


def go(nfaces, ndice, ntop, desiredsum):
    v = {(): 1}

    for i in range(ndice):
        v = step(v, range(1, nfaces + 1), ntop)
        print(len(v))

    totalcount = 0
    for top, count in v.items():
        if sum(top) == desiredsum:
            totalcount += count

    return totalcount


print(go(12, 20, 10, 70))
