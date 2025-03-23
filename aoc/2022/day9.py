fname = "day9_input.txt"
#fname = "day9_example.txt"
data = [s.strip().split() for s in open(fname).readlines()]

for v in data:
    v[1] = int(v[1])

class Rope:
    def __init__(self, knot_count):
        self.x, self.y = [0] * knot_count, [0] * knot_count
        self.knot_count = knot_count
        self.tail_count = knot_count - 1
        
        self.tail_path = {(0, 0)}

    def motion(self, dir, count):
        for _ in range(count):
            match dir:
                case "U":
                    self.y[0] -= 1
                case "D":
                    self.y[0] += 1
                case "L":
                    self.x[0] -= 1
                case "R":
                    self.x[0] += 1

            for i in range(self.tail_count):
                if max(abs(self.x[i] - self.x[i+1]), abs(self.y[i] - self.y[i+1])) > 1:
                    self.x[i+1] += 1 if self.x[i+1] < self.x[i] else -1 if self.x[i+1] > self.x[i] else 0
                    self.y[i+1] += 1 if self.y[i+1] < self.y[i] else -1 if self.y[i+1] > self.y[i] else 0
            self.tail_path.add((self.x[self.tail_count], self.y[self.tail_count]))



def problim(data, knot_count):
    rope = Rope(knot_count)
    for move in data:
        rope.motion(*move)
    print(len(rope.tail_path))

problim(data, 2)
problim(data, 10)
