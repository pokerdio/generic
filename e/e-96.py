import copy


def friendsof(x, y):
    x0, y0 = x // 3, y // 3
    for i in range(3):
        for j in range(3):
            yield x0 * 3 + i, y0 * 3 + j


class SuDoku:
    def Key(self):
        assert(self.solved == True)
        lst = self.solution.table[0]
        return lst[0] * 100 + lst[1] * 10 + lst[2]

    def DecideIfSolved(self):
        for y in range(9):
            for x in range(9):
                value = self.table[y][x]
                if type(value) == set:
                    if not value:
                        self.solved = False
                        return False
                    assert(len(value) > 1)
                    self.solved = None
                    return None

        self.solution = self
        self.solved = True
        return True

    def Deduction(self):
        while True:
            if self.FindImpossible():
                self.solved = False
                return
            xy = self.FindMonoSet()
            if xy:
                x, y = xy
                lst = self.table[y]
                value = lst[x]
                assert(type(value) == set and len(value) == 1)
                lst[x] = value.pop()
                self.Prune(x, y)
            else:
                self.DecideIfSolved()
                if self.solved == None:
                    self.Backtracking()
                return

    def InitList(self, v81):
        self.table = [[] for x in range(9)]
        k = 0
        for y in range(9):
            for x in range(9):
                value = v81[k]
                if type(value) == str:
                    value = int(value)
                if value == 0:
                    value = set(range(1, 10))
                self.table[y].append(value)
                k += 1

        for y in range(9):
            for x in range(9):
                value = self.table[y][x]
                if type(value) == int:
                    self.Prune(x, y)
        self.Deduction()

    def FindMonoSet(self):
        for y in range(9):
            for x in range(9):
                value = self.table[y][x]
                if type(value) == set and len(value) == 1:
                    return x, y

    def FindImpossible(self):
        for y in range(9):
            for x in range(9):
                value = self.table[y][x]
                if type(value) == set and not value:
                    return x, y

    def InitOther(self, sudoku, x, y, value):
        self.table = copy.deepcopy(sudoku.table)
        self.table[y][x] = value
        assert(type(value) == int)
        self.Prune(x, y)
        self.Deduction()

    def FindMinSet(self):
        best = 10
        for y in range(9):
            for x in range(9):
                value = self.table[y][x]
                if type(value) == set and len(value) < best:
                    best = len(value)
                    best_value = value
                    bestx, besty = x, y
        return bestx, besty

    def Backtracking(self):
        x, y = self.FindMinSet()
        value = self.table[y][x]

        for v in value:
            sudoku = SuDoku(self, x, y, v)
            if sudoku.solved == True:
                self.solution = sudoku.solution
                self.solved = True
                return
        self.solved = False

    def __init__(self, v81, *args):
        if type(v81) == list or type(v81) == str:
            self.InitList(v81)
        elif type(v81) == SuDoku:
            self.InitOther(v81, * args)

    def Prune(self, x, y):
        value = self.table[y][x]
        assert(type(value) == int)
        for i in range(9):
            v = self.table[y][i]
            if type(v) == set:
                v.discard(value)
            v = self.table[i][x]
            if type(v) == set:
                v.discard(value)

        for a, b in friendsof(x, y):
            v = self.table[b][a]
            if type(v) == set:
                v.discard(value)


def read1(fname="p096_sudoku.txt"):
    with open(fname) as f:
        v = []
        firstline = True
        for s in f.readlines():
            if firstline:
                firstline = False
            else:
                v.append(s.strip())
                if len(v) == 9:
                    yield("".join(v))
                    v = []
                    firstline = True


def read0():
    return next(read1("euler96.txt"))


def read2():
    r = read1()
    next(r)
    return next(r)


z = [SuDoku(x).Key() for x in read1()]
print(sum(z))
