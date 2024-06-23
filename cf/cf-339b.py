n, m = (int(c) for c in input().split())
v = [int(c) for c in input().split()]

last = 1
total_time = 0
for house in v:
    if house >= last:
        total_time += house - last
    else:
        total_time += n - last + house

    last = house
print(total_time)
