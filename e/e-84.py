from prob import RStateMachine as RSM


board = ["GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
         "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
         "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
         "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"]


def idx(name, pos=0):
    if name in board:
        return board.index(name)
    for i in range(40):
        if board[(pos + i) % 40].startswith(name):
            return (pos + i) % 40


def roll(x0, dice_sides):

    square = dice_sides ** 2
    p = 1.0 / square
    p15 = p * ((square - 1.0) / square)
    p01 = p * (1.0 / square)

    ret = [0.0] * 40

    for i in range(1, dice_sides + 1):
        for j in range(1, dice_sides + 1):
            if i != j:
                ret[(x0 + i + j) % 40] += p
            else:
                ret[(x0 + i + j) % 40] += p15
                ret[idx("JAIL")] += p01

    for i in range(40):
        if board[i].startswith("CC"):
            ret[idx("GO")] += ret[i] / 16.0
            ret[idx("JAIL")] += ret[i] / 16.0
            ret[i] *= (14.0 / 16.0)

        if board[i].startswith("CH"):
            for s in ["GO", "JAIL", "C1", "E3", "H2", "R1"]:
                ret[idx(s)] += ret[i] / 16.0
            ret[idx("R", i)] += ret[i] / 8.0
            ret[idx("U", i)] += ret[i] / 16.0
            goback3 = (i + 37) % 40
            ret[goback3] += ret[i] / 16.0
            if board[goback3].startswith("CC"):
                ret[idx("GO")] += ret[i] / 16.0 / 16.0
                ret[idx("JAIL")] += ret[i] / 16.0 / 16.0
                ret[goback3] -= ret[i] / 16.0 / 8.0

            ret[i] *= (6.0 / 16.0)

    ret[idx("JAIL")] += ret[idx("G2J")]
    ret[idx("G2J")] = 0
    return ret


def go(dice_sides=4):
    r = RSM(40)
    for i in range(40):
        r.Outcome(i, zip(roll(i, dice_sides), range(40)))
    sol = r.Solve()

    print("".join(["%02d" % i[1] for i in sorted(list(zip(sol, range(40))),
                                                 key=lambda pair: 1.0 - pair[0])[:3]]))
    return sol
