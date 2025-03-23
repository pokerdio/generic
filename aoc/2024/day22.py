secret = [int(x) for x in open("day22_input.txt").readlines()]

def mix(i, j):
    return (i ^ j) % 16777216

def nextSecret(i):
    i = mix(i, i * 64)
#    i = mix(i, (i + 15) // 32)
    i = mix(i, i // 32)
    i = mix(i, i * 2048)
    return i
    
def next2000(i):
    for _ in range(2000):
        i = nextSecret(i)
    return i

def bananas(i, counter):
    cur = ()
    banned = set()

    for _ in range(2000):
        j = nextSecret(i)
        cur = cur + ((i % 10)-(j % 10),)
        if len(cur) == 4 and not cur in banned: 
            banned.add(cur)
            counter[cur] = counter.get(cur, 0) + (j % 10)
        i = j
        cur = cur[-3:]


print(sum(next2000(s) for s in secret))

counter = {}
for i in secret:
    bananas(i, counter)

print(counter[max(counter, key=lambda x:counter[x])])
