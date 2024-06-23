
d = {"Ac": 89, "Ag": 47, "Al": 13, "Am": 95, "Ar": 18, "As": 33, "At": 85,
     "Au": 79, "B": 5, "Ba": 56, "Be": 4, "Bh": 107, "Bi": 83, "Bk": 97,
     "Br": 35, "C": 6, "Ca": 20, "Cd": 48, "Ce": 58, "Cf": 98, "Cl": 17,
     "Cm": 96, "Co": 27, "Cr": 24, "Cs": 55, "Cu": 29, "Ds": 110, "Db": 105,
     "Dy": 66, "Er": 68, "Es": 99, "Eu": 63, "F": 9, "Fe": 26, "Fm": 100,
     "Fr": 87, "Ga": 31, "Gd": 64, "Ge": 32, "H": 1, "He": 2, "Hf": 72,
     "Hg": 80, "Ho": 67, "Hs": 108, "I": 53, "In": 49, "Ir": 77, "K": 19,
     "Kr": 36, "La": 57, "Li": 3, "Lr": 103, "Lu": 71, "Md": 101, "Mg": 12,
     "Mn": 25, "Mo": 42, "Mt": 109, "N": 7, "Na": 11, "Nb": 41,
     "Nd": 60, "Ne": 10, "Ni": 28, "No": 102, "Np": 93, "O": 8, "Os": 76,
     "P": 15, "Pa": 91, "Pb": 82, "Pd": 46, "Pm": 61, "Po": 84, "Pr": 59,
     "Pt": 78, "Pu": 94, "Ra": 88, "Rb": 37, "Re": 75, "Rf": 104, "Rg": 111,
     "Rh": 45, "Rn": 86, "Ru": 44, "S": 16, "Sb": 51, "Sc": 21, "Se": 34,
     "Sg": 106, "Si": 14, "Sm": 62, "Sn": 50, "Sr": 38, "Ta": 73, "Tb": 65,
     "Tc": 43, "Te": 52, "Th": 90, "Ti": 22, "Tl": 81, "Tm": 69, "U": 92,
     "V": 23, "W": 74, "Xe": 54, "Y": 39, "Yb": 70, "Zn": 30, "Zr": 40}

v = [0] * (max(d.values()) + 1)
for s, n in d.items():
    v[n] = s


def input_iter():
    while True:
        yield input()


def s_iter():
    yield "10 3"
    yield "Mn Co Li Mg C P F Zn Sc K"
    yield "Sn Pt Y"


# def s_iter():
#     yield "2 1"
#     yield "H H"
#     yield "He"


# def s_iter():
#     yield "2 2"
#     yield "Bk Fm"
#     yield "Cf Es"


def synth(feed, atom_type, min_feed=0):
    assert(type(feed) == dict)
    if atom_type <= min_feed:
        return
    if atom_type in feed and feed[atom_type] > 0:
        feed[atom_type] -= 1
        yield (atom_type,)
        feed[atom_type] += 1
        return
    feed_keys = [x for x in feed.keys() if feed[x] > 0 and x > min_feed and x <= atom_type]
    feed_total = sum(feed[x] * x for x in feed_keys)
    if feed_total < atom_type:
        return
    for key in feed_keys:
        count = feed[key]
        tup = ()
        for i in range(1, count + 1):
            tup += (key,)
            if i * key > atom_type:
                break
            if i * key == atom_type:
                feed[key] -= i
                yield tup
                feed[key] = count
                break
            if feed_total - (count - i) * key >= atom_type and atom_type - key * i > key:
                feed[key] -= i
                for c in synth(feed, atom_type - key * i, key):
                    yield tup + c
                feed[key] = count


def synth_go(feed, atoms, build=()):
    next = atoms[1:]
    for c in synth(feed, atoms[0]):
        b = (*build, (atoms[0], c))
        if next:
            synth_go(feed, next, b)
        else:
            #print("success", b)
            raise Exception(b)


def go(o=s_iter()):
    n, k = [int(x) for x in next(o).split()]
    v0 = sorted([d[x] for x in next(o).split()])
    v1 = [d[x] for x in next(o).split()]

    d0 = {}
    for x in v0:
        d0[x] = d0.get(x, 0) + 1

    try:
        synth_go(d0, v1)
    except Exception as e:
        print("YES")
        for a, b in e.args[0]:
            print("%s->%s" % ("+".join([v[x] for x in b]), v[a]))
        return
    print("NO")


go(input_iter())
