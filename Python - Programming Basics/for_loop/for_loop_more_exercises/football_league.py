stadium_capacity = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for seats in range(1, number_of_fans + 1):
    sector_seat = input()
    if sector_seat == 'A':
        sector_a += 1
    elif sector_seat == 'B':
        sector_b += 1
    elif sector_seat == 'V':
        sector_v += 1
    else:
        sector_g += 1

fans_to_stadium_ratio = number_of_fans / stadium_capacity * 100
percent_a = sector_a / number_of_fans * 100
percent_b = sector_b / number_of_fans * 100
percent_v = sector_v / number_of_fans * 100
percent_g = sector_g / number_of_fans * 100


print(f'{percent_a:.2f}%')
print(f'{percent_b:.2f}%')
print(f'{percent_v:.2f}%')
print(f'{percent_g:.2f}%')
print(f'{fans_to_stadium_ratio:.2f}%')




