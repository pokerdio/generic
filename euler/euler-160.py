class Solve():
    def pow_div_100k(n, k):
        n %= 100000
        v = [n]
        two = 1
        while two < k:
            two = two * 2
            v.append(v[-1] ** 2 % 100000)

        two, ret, i = 1, 1, 0
        while two <= k:
            if k & two:
                ret = ret * v[i] % 100000
            two *= 2
            i += 1
        return ret

    def test_pow_div_100k():
        pw = Solve.pow_div_100k
        for j in [0, 1, 6, 17, 117]:
            for i in range(j, 10**5, 10**3):
                for k in [0, 1, 6, 17, 29, 117]:
                    for q in range(k, 10**3, 73):
                        assert (pw(i, q) == (i**q) % 100000)

    def init_odds(self):
        """odds from 1 to 100000 is odds from 2*0+1..2*49999+1
        v[0]->1 v[1]->3 v[2]->5... v[49999]->99999
        fives not included"""
        v = [0] * 50000
        p = 1
        for i in range(0, 50000):
            k = 2 * i + 1
            if k % 5 != 0:
                p = p * k % 100000
            v[i] = p
        self.odds = v

    def init_conti(self):
        """nums from 1 to 100000
        v[0]->1 v[99999]->100000
        fives and tens not included"""
        v = [0] * 100000

        p = 1
        for i in range(0, 100000):
            k = i + 1
            if k % 5 != 0:
                p = p * k % 100000
            v[i] = p
        self.conti = v

    def go_conti(self, n):
        """1..n product inclusive"""
        print("enter conti", n)
        p1, twos1, p2, twos2 = 1, 0, 1, 0
        if n >= 10:  # tens go recursive
            p1, twos1 = self.go_conti(n // 10)

        if n >= 5:
            fives = (n + 5) // 10
            p2, twos2 = self.go_odds(fives * 2 - 1)
            twos2 += fives

        n_conti = len(self.conti)
        k = n - 1
        if k < n_conti:
            p3 = self.conti[k]
        else:
            p3 = self.conti[k % n_conti] * Solve.pow_div_100k(self.conti[-1], k // n_conti)
            p3 %= 100000

        ret = p1 * p2 * p3 % 100000
        ret_twos = twos1 + twos2
        print("exit conti", n, ret, ret_twos)
        return ret, ret_twos

    def go_odds(self, n):
        """odds from 1 to n, n inclusive"""
        print("enter odds", n)
        fives = ((n + 5) // 10)
        if fives:
            p1, twos = self.go_odds(fives * 2 - 1)
            twos += fives
        else:
            p1, twos = 1, 0

        k = (n - 1) // 2
        n_odds = len(self.odds)

        if k < n_odds:
            p2 = self.odds[k]
        else:
            #p2 = self.odds[k % n_odds] * (self.odds[-1] ** (k // n_odds) % 100000) % 100000
            p2 = self.odds[k % n_odds] * Solve.pow_div_100k(self.odds[-1], k // n_odds)
            p2 %= 100000

        ret = (p1 * p2 % 100000)
        print("exit odds", n, ret, twos)
        return ret, twos

    def __init__(self):
        self.init_odds()
        self.init_conti()
#        Solve.test_pow_div_100k()

    def go(self, n=10**6):
        two_bank = n // 2  # we steal twos from the 2,4,8,6,... numbers in the product
        # 2*4*..n = 2**n * (1*2*3*..*n//2)
        # leftovers are 1 3 5..n-1

        p1, two1 = self.go_odds(n)
        p2, two2 = self.go_conti(n // 2)
        two_bank -= two1 + two2
        assert(two_bank > 0)
        return (p1 * p2 * Solve.pow_div_100k(2, two_bank)) % 100000


print(Solve().go(10**12))
