#!/usr/bin/env python3

# read csv names from p022_names.txt


a, b = 1, 1
k = 2
threshold = 10**999


while True:
    a, b, k = a + b, a, k + 1
    if a >= threshold:
        print(k)
        break
