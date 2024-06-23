noms = [tuple([int(c) for c in s.strip()]) for s in open("p079_keylog.txt").readlines()]

noms_set = set(noms)
letters = set.union(*(set(nom) for nom in noms))

for a, b, c in noms:
    noms_set.add((a, b))
    noms_set.add((a, c))
    noms_set.add((b, c))
    noms_set.add((a, ))
    noms_set.add((b, ))
    noms_set.add((c, ))


def son_of_a(small_tuple, big_tuple):
    k = 0
    for c in small_tuple:
        try:
            k = big_tuple.index(c)
            big_tuple = big_tuple[k + 1:]
        except:
            return False
    return True


def score(password):
    global noms_set
    s = 0
    for nom in noms_set:
        if son_of_a(nom, password):
            s = s + 1
#    print("score of", password, "is", s)
    return s


def step(password):
    global letters, noms_set
    best = -1
    bestpas = None
    for k in range(len(password) + 1):
        for c in letters:
            newpas = password[:k] + (c, ) + password[k:]
            newpas_score = score(newpas)
            if newpas_score > best:
                best = newpas_score
                bestpas = newpas
    if best == len(noms_set):
        print("final solution")
    return bestpas
