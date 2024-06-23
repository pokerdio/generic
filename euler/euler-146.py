from random import randint


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while b > 0:
        a, b = b, a % b
    return a


def kapow(a, b, p):
    twos = []
    ret = 1

    while b > 0:
        if b % 2 == 1:
            ret = (ret * a) % p
        a = a * a % p
        b //= 2
    return ret


def fermat2(p, a=2):

    if gcd(a, p) > 1:
        return False

    return kapow(a, p - 1, p) == 1



def rm_prime(n, attempts = 3):
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3
    if n % 5 == 0:
        return n == 5


    n1 = n - 1
    m = n1
    twos = 0
    while m % 2 == 0:
        m //= 2
        twos += 1


    base = 2
    for _ in range(attempts):
        k = kapow(base, m, n)
        

        alarm = k > 1 and k < n1

        for _ in range(twos):
            if k == n1:
                alarm = False
            elif k == 1:
                if alarm:
                    return False
                else:
                    break
            k = k * k % n
        else:
            if k != 1:
                return False
        if base < 4:
            base += 1
        else:
            base = randint(5, n1 - 1)
    return True



def go(n):
    yas = [1, 3, 7, 9, 13, 27]
    nay = [11, 17, 19, 21, 23]
    for i in range(1, n // 10):
        i2 = (i * 10) ** 2
        if i % 100 == 0:
            print(i)
        for p in yas:
            if not rm_prime(i2 + p, 15):
                break
        else:
            for p in nay:
                if rm_prime(i2 + p, 15):
                    break
            else:
                yield i * 10
        


arnault = 69876422826251144928143383863659397076940401

