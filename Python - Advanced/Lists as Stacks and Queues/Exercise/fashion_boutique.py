clothes = [int(x) for x in input().split()]

max_rack = int(input())
racks = 1
rack_space = max_rack

while clothes:

    cloth = clothes.pop()

    if rack_space >= cloth:
        rack_space -= cloth
    else:
        racks += 1
        rack_space = max_rack - cloth

print(racks)


