fire_level = input().split('#')
water = int(input())
effort = 0
total_fire = 0
cells_put_out = []

for fires in fire_level:
    info_is_true = False
    fire_info = fires.split(' = ')
    fire_int = int(fire_info[1])
    if fire_info[0] == 'Low' and 1 <= fire_int <= 50:
        info_is_true = True
    elif fire_info[0] == 'Medium' and 51 <= fire_int <= 80:
        info_is_true = True
    elif fire_info[0] == 'High' and 81 <= fire_int <= 125:
        info_is_true = True
    else:
        continue

    if water >= fire_int:
        if info_is_true:
            water -= fire_int
            cells_put_out.append(fire_int)
            total_fire += fire_int
            effort += fire_int * 0.25


print(f'Cells:')
for i in range(len(cells_put_out)):
    print(f' - {cells_put_out[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')