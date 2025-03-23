input = [[int(x) for x in s.strip().split()] for s in open("day2_input.txt").readlines()]

def safe(v):
    v = [v[i] - v[i + 1] for  i in range(len(v) - 1)]
    if v[0] > 0:
        return min(v) >= 1 and max(v) <= 3
    else:
        return min(v) >= -3 and max(v) <= -1


print(sum(safe(report) for report in input))


def safe2(v): # O(n) possible, but O(n*n) is easier to write
    for i in range(len(v)):
        if safe(v[:i] + v[i+1:]):
            return True
    return False

print(sum(safe2(report) for report in input))
