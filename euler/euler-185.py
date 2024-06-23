from collections import Counter

txt = """5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct"""

# txt = """90342 ;2 correct
# 70794 ;0 correct
# 39458 ;2 correct
# 34109 ;1 correct
# 51545 ;2 correct
# 12531 ;1 correct"""


s = [[int(a) for a in c.split()[0]] for c in txt.splitlines()]
kor = [int(c.split()[1][1:]) for c in txt.splitlines()]


def p(n):
    for i in range(len(s)):
        if kor[i] == n:
            print("".join(str(x) for x in s[i]))


def foo(n):
    for i in range(len(s[0])):
        c = Counter(s[j][i] for j in range(len(s)) if kor[j] >= n)
        print({x: y for x, y in c.items() if y > 1})


def go(digit, s, correct):
    if digit == len(s[0]):
        if (not sum(correct)):
            yield ()
        return

    ban = set(s[i][digit] for i in range(len(s)) if not correct[i])
    if digit == 0:
        ban.add(0)
    if digit == 8:
        print(len(ban), correct)
    for d in (9, 1, 0, 2, 3, 4, 5, 6, 7, 8):
        if d not in ban:
            c2 = correct.copy()
            for i in range(len(s)):
                if s[i][digit] == d:
                    c2[i] -= 1
            for combo in go(digit + 1, s, c2):
                yield (d, *combo)


def assume(digit, value, s, allow)
