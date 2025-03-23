farm = open("day12_input.txt").read().split()

width, height = len(farm[0]), len(farm)
region = [[-1] * width for _ in range(height)]
region_count = 0
region_area = {}

def neigh(x, y):
    global width, height
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        x1, y1 = x + dx, y + dy
        if x1 >= 0 and y1 >= 0 and x1 < width and y1 < height:
            yield (x1, y1)

def fence_count(x, y):
    global farm
    neigh_count = 0
    ret = 0
    for x1, y1 in neigh(x, y):
        neigh_count += 1
        if farm[y][x] != farm[y1][x1]:
            ret += 1
    return ret + (4 - neigh_count)
        

fence_ban_dict = set()

def side_count(x, y): 
    # this assumes that the function is called in ascending order of x, y pairs
    global farm, fence_ban_dict, width, height
    ret = 0
    plant = farm[y][x]
    # above
    if (x, y, "above") not in fence_ban_dict: 
        if y == 0: 
            ret += 1
            for x2 in range(x+1, width):
                if farm[y][x2] == plant:
                    fence_ban_dict.add((x2, y, "above"))
                else:
                    break
        else: 
            if plant != farm[y-1][x]:
                ret += 1
                for x2 in range(x+1, width):
                    if farm[y][x2] == plant and farm[y-1][x2] != plant:
                        fence_ban_dict.add((x2, y, "above"))
                    else:
                        break

    # below
    if (x, y, "below") not in fence_ban_dict: 
        if y == height-1: 
            ret += 1
            for x2 in range(x+1, width):
                if farm[y][x2] == plant:
                    fence_ban_dict.add((x2, y, "below"))
                else:
                    break
        else: 
            if plant != farm[y+1][x]:
                ret += 1
                for x2 in range(x+1, width):
                    if farm[y][x2] == plant and farm[y+1][x2] != plant:
                        fence_ban_dict.add((x2, y, "below"))
                    else:
                        break


    # left
    if (x, y, "left") not in fence_ban_dict: 
        if x == 0: 
            ret += 1
            for y2 in range(y+1, height):
                if farm[y2][x] == plant:
                    fence_ban_dict.add((x, y2, "left"))
                else:
                    break
        else: 
            if farm[y][x-1] != plant: 
                ret += 1
                for y2 in range(y+1, height):
                    if farm[y2][x] == plant and farm[y2][x-1] != plant:
                        fence_ban_dict.add((x, y2, "left"))
                    else:
                        break


    # right
    if (x, y, "right") not in fence_ban_dict: 
        if x == width-1: 
            ret += 1
            for y2 in range(y, height):
                if farm[y2][x] == plant:
                    fence_ban_dict.add((x, y2, "right"))
                else:
                    break
        else: 
            if farm[y][x+1] != plant: 
                ret += 1
                for y2 in range(y, height):
                    if farm[y2][x] == plant and farm[y2][x+1] != plant:
                        fence_ban_dict.add((x, y2, "right"))
                    else:
                        break
    return ret
    

def expandRegion(x, y):
    global region_count, region_area, farm, region
    plant = farm[y][x]
    reg_id = region_count
    region_count += 1
    region_area[reg_id] = 0

    open = {(x, y)}
    while open:
        x, y = open.pop()
        region[y][x] = reg_id
        region_area[reg_id] += 1
        for x2, y2 in neigh(x, y): 
            if (plant == farm[y2][x2] and -1 == region[y2][x2]):
                open.add((x2, y2))


def problim():
    global width, height, region_count, region_area


    for y in range(height):
        for x in range(width):
            if region[y][x] == -1:
                expandRegion(x, y)


    region_perimeter = [0] * region_count
    region_perimeter2 = [0] * region_count

    for y in range(height):
        for x in range(width):
            region_perimeter[region[y][x]] += fence_count(x, y)
            region_perimeter2[region[y][x]] += side_count(x, y)
    ret = 0
    print(sum(region_area[reg_id] * region_perimeter[reg_id] for reg_id in range(region_count)))
    print(sum(region_area[reg_id] * region_perimeter2[reg_id] for reg_id in range(region_count)))



