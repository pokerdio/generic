#!/usr/bin/env python3

#
total = 0

for i in range(1, 1000000):
    dec = str(i)
    binary = format(i, "b")
    if dec == "".join(reversed(dec)) and binary == "".join(reversed(binary)):
        print(dec, binary)
        total = total + i


print(total)
