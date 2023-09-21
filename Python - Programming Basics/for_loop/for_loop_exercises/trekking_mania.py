number_of_groups = int(input())
total_climbers = 0
g1 = 0
g2 = 0
g3 = 0
g4 = 0
g5 = 0

for num in range(number_of_groups):
    groups = int(input())
    total_climbers += groups
    if groups <= 5:
        g1 += groups
    elif groups <= 12:
        g2 += groups
    elif groups <= 25:
        g3 += groups
    elif groups <= 40:
        g4 += groups
    elif groups >= 41:
        g5 += groups

print(f'{g1 / total_climbers * 100:.2f}%')
print(f'{g2 / total_climbers * 100:.2f}%')
print(f'{g3 / total_climbers * 100:.2f}%')
print(f'{g4 / total_climbers * 100:.2f}%')
print(f'{g5 / total_climbers * 100:.2f}%')

