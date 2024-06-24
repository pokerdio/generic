def score(hand):
    pass


def card_num(card):
    try:
        return int(card[0])
    except:
        return "TJQKA".find(card[0]) + 10


def signature(v):
    d = {}
    for s in v:
        d[s] = 1 + d.get(s, 0)

    return tuple(reversed(sorted(d.values())))


def straight(v):
    v = sorted(v)
    return [v[i + 1] - v[i] for i in range(4)] == [1, 1, 1, 1]


def score(hand, lookup={(1, 1, 1, 1, 1): 0, (2, 1, 1, 1): 1, (2, 2, 1): 2,
                        (3, 1, 1): 3, (3, 2): 6, (4, 1): 7}):

    v = [card_num(card) for card in hand]
    vcount = {i: v.count(i) for i in set(v)}

    s = lookup[signature(v)]
    if straight(v):
        s += 4
    if len(set(card[1] for card in hand)) == 1:
        s += 5  # flush

    return (s, *list(reversed(sorted(v, key=lambda x: (vcount[x], x)))))


def go_line(line):
    twohands = line.strip().split()
    print(score(twohands[:5]), score(twohands[5:]),
          score(twohands[:5]) > score(twohands[5:]))
    return score(twohands[:5]) > score(twohands[5:])


def go():
    total = 0
    for s in open("p054_poker.txt").readlines():
        total += go_line(s)
    return total
