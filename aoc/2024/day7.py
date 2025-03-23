import re
v = [[int(n) for n in re.split("[ :]+", s.strip())] for s in open("day7_input.txt").readlines()]

def tryPlusMul(target, current, v, v_idx):
    if v_idx == len(v):
        return target == current

    newCurrent = v[v_idx] + current
    if newCurrent <= target and tryPlusMul(target, newCurrent, v, v_idx + 1):
        return True

    newCurrent = v[v_idx] * current
    if newCurrent <= target and tryPlusMul(target, newCurrent, v, v_idx + 1):
        return True
    return False
        
def tryLine(v):
    if len(v) == 2:
        return v[0] == v[1]

    return tryPlusMul(v[0], v[1], v, 2)


answer = 0
for i in range(len(v)):
    if tryLine(v[i]):
        answer += v[i][0]

print(answer)
