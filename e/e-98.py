import math


def git_words():
    with open("p098_words.txt") as f:
        return [s.strip('", ') for s in f.read().split(",")]


def encode_words(words):
    words = git_words()

    d = {}
    for w in words:
        code = "".join(sorted(w))
        if code in d:
            d[code].append(w)
        else:
            d[code] = [w]
    return {a: b for a, b in d.items() if len(b) > 1}


words = git_words()
words_code = encode_words(words)

words = sum(list(words_code.values()))

max_word_len = max(len(w) for w in words_code.keys())

squares = [x**2 for x in range(1, 1 + int(math.sqrt(int("9" * max_word_len))))]


def getpat(s):
    s = str(s)
    a = ord("a")
    pat = ""
    x = {}
    for c in s:
        if c not in x:
            x[c] = chr(a)
            a += 1

        pat += x[c]
    return pat


num_pats = {}

for sq in squares:
    s = getpat(sq)
    if s in num_pats:
        num_pats[s].append(sq)
    else:
        num_pats[s] = [sq]


word_pats = {}


for w in words:
    word_pats[w] = getpat(w)


solutions = []


def translate(n, w1, w2):
    n = str(n)
    assert(len(n) == len(w1))

    dic = {}
    for d, c in zip(n, w1):
        dic[c] = d

    n2 = int("".join(dic[c] for c in w2))
    if len(str(n2)) == len(n):
        return n2


max_solution = -1

for wlist in words_code.values():
    wlen = len(wlist)

    for i in range(wlen - 1):
        for j in range(i + 1, wlen):
            w1, w2 = wlist[i], wlist[j]
            for n1 in num_pats[word_pats[w1]]:
                n2 = translate(n1, w1, w2)
                if n2 in squares and n2 > n1:
                    solutions.append((n1, w1, n2, w2))
                    max_solution = max(max_solution, n1, n2)


print("dee answah issa ", max_solution)
