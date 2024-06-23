v = [c == '1' for c in input()]
weights = [x + 1 for x in range(10) if v[x]]
m = int(input())


def expand(state):
    last_weight, delta, history = state
    for w in weights:
        if w > delta and w != last_weight:
            yield w, w - delta, history + [(last_weight, delta)]


def solution(state, m=m):
    w, delta, history = state
    if len(history) == m:
        return [history[x][0] for x in range(1, m)] + [w]
    if (w, delta) in history:
        idx_start = history.index((w, delta))
        idx_stop = len(history)
        i = idx_start
        while len(history) <= m:
            history.append(history[i])
            i += 1
            if i >= idx_stop:
                i = idx_start
        return [h[0] for h in history[1:]]


def go():
    state_open = [[0, 0, []]]
    while state_open:
        state = state_open.pop(0)
        for new_state in expand(state):
            # print(new_state)
            v = solution(new_state)
            if v:
                print("YES")
                print(" ".join(str(x) for x in v))
                return True
            state_open.append(new_state)


if not go():
    print("NO")
