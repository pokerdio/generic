import re
input = open("day13_input.txt").readlines()
n = (len(input) + 1) // 4


def getInts(s):
    v = re.match("[^0-9]*([0-9]+)[^0-9]+([0-9]+)", s)
    return list(int(x) for x in v.groups())

class GameMachine():
    def __init__(self, sv):
        self.Adx, self.Ady = getInts(sv[0])
        self.Bdx, self.Bdy = getInts(sv[1])
        self.prize_x, self.prize_y = getInts(sv[2])

    def __repr__(self):
        return f'''Button A: X+{self.Adx}, Y+{self.Ady}
Button B: X+{self.Bdx}, Y+{self.Bdy}
Prize: X={self.prize_x}, Y={self.prize_y}'''

    def solve(self):
        '''returns cheapest way to win or none'''
        self.prize_x %= 10000000000000
        self.prize_y %= 10000000000000

        for a in range(0, 101):
            if (a * self.Adx > self.prize_x) or (a * self.Ady > self.prize_y):
                break
            dx = self.prize_x - a * self.Adx
            dy = self.prize_y - a * self.Ady

            b = dx // self.Bdx

            if b > 100:
                continue

            if self.Bdx * b == dx and self.Bdy * b == dy:
                return a * 3 + b # smallest a means smallest token cost

        return 0

    
    def solve2(self):
        '''returns cheapest way to win or none'''
        
        self.prize_x = 10000000000000 + (self.prize_x % 10000000000000)
        self.prize_y = 10000000000000 + (self.prize_y % 10000000000000)

        open = [('', '')]
        for digit in range(1, 16):
            ten_digit = 10 ** digit
            new_open = []
#            print(digit, open)
            for sa, sb in open: 
                for a in range(10):
                    for b in range(10):
                        sa2 = str(a) + sa
                        sb2 = str(b) + sb
                        a2, b2 = int(sa2), int(sb2)
                        valx = a2 * self.Adx + b2 * self.Bdx
                        valy = a2 * self.Ady + b2 * self.Bdy
                        if valx == self.prize_x and valy == self.prize_y:
                            return a2 * 3 + b2
                        if valx < self.prize_x and valy  < self.prize_y and \
                           self.prize_x % ten_digit == valx % ten_digit and \
                           self.prize_y % ten_digit == valy % ten_digit:
                            new_open.append((sa2, sb2))
            open = new_open
        return 0



m = [GameMachine(input[x:x+4]) for x in range(0, n * 4, 4)]
print(sum(m.solve() for m in m))
print(sum(m.solve2() for m in m))

# GameMachine('''Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# '''.split('\n')).solve2()
