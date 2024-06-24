#!/usr/bin/env python3

#


def penta(n):
    return n * (3 * n - 1) // 2


def tri(n):
    return n * (n + 1) // 2


def hexa(n):
    return n * (2 * n - 1)


class Clicker:
    def __init__(self, fun, n0):
        self.fun = fun
        self.n = n0
        self.value = fun(n0)

    def click(self):
        self.n = self.n + 1
        self.value = self.fun(self.n)

    def __repr__(self):
        return str(self.fun.__name__) + " " + str(self.n) + " " + str(self.value)


v = [Clicker(tri, 1), Clicker(penta, 1), Clicker(hexa, 1)]

while True:
    if v[0].value == v[1].value and v[1].value == v[2].value:
        print("equality at", v)
    min(v, key=lambda x: x.value).click()
