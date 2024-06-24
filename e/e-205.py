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


def dooit():
    pete = dice(list(range(1, 5)), 9)
    colin = dice(list(range(1, 7)), 6)

    colinsum = colin[0]
    petewins = 0

    for s in range(1, 37):
        petewins += pete[s] * colinsum
        colinsum += colin[s]

    print("%0.7f" % (petewins / sum(colin) / sum(pete)))


dooit()
