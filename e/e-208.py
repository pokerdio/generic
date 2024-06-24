# 0 -> 1 +a ; 4 +e
# 1 -> 2 +b ; 0 +a
# 2 -> 3 +c ; 1 +b
# 3 -> 4 +d ; 2 +c
# 4 -> 0 +e ; 3 +d


def foo():
    v = []
    for i in range(5):
        left = ((i + 1) % 5, i)
        right = ((i + 4) % 5, (i + 4) % 5)
        v.append((left, right))

    return v


def go(n):
    t = foo()
    v = {(0, 0, 0, 0, 0, 0): 1}
    n5 = n // 5
    for _ in range(n):
        v2 = {}
        for state, paths in v.items():
            for direction, delta in t[state[0]]:
                state2 = (direction, (delta == 0) + state[1],
                          (delta == 1) + state[2], (delta == 2) + state[3],
                          (delta == 3) + state[4], (delta == 4) + state[5])
                if max(state2[1:]) <= n5:
                    v2[state2] = v2.get(state2, 0) + paths
        v = v2
    want = (n5, ) * 5
    return (v[(0, *want)])
