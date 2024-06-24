#!/usr/bin/env python3


teens = (" one two three four five six seven eight "
         "nine ten eleven twelve thirteen fourteen fifteen "
         "sixteen seventeen eighteen nineteen").split(" ")

# explicitly calling split with a space character makes an empty
# string at zero which is useful to us

tens = " ten twenty thirty forty fifty sixty seventy eighty ninety".split(" ")


def NumberToWords(n):
    if n < 20:
        return teens[n]
    if n < 100:
        return tens[n // 10] + teens[n % 10]
    if n < 1000:
        return teens[n // 100] + " hundred" + \
            (" and " + NumberToWords(n % 100) if n % 100 > 0 else "")
    return "one thousand"


print()


def LettersInRange(start, stop=-1):
    if stop < 0:
        stop = start + 1
    return len("".join((NumberToWords(x) for x in range(start, stop))).replace(" ", ""))


print(LettersInRange(1, 1001))
