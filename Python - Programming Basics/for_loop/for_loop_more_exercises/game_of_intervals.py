game_turns = int(input())

total_turns = 0
invalid_numbers = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
total_points = 0

for turns in range(1, game_turns + 1 ):
    number = int(input())
    total_turns += 1
    if 0 > number or number > 50:
        invalid_numbers += 1
        total_points /= 2
    else:
        if 0 <= number <= 9:
            from_0_to_9 += 1
            total_points += number * 0.20
        elif number <= 19:
            from_10_to_19 += 1
            total_points += number * 0.30
        elif number <= 29:
            from_20_to_29 += 1
            total_points += number * 0.40
        elif number <= 39:
            from_30_to_39 += 1
            total_points += 50
        elif number <= 50:
            from_40_to_50 += 1
            total_points += 100

print(f'{total_points:.2f}')
print(f'From 0 to 9: {from_0_to_9 / total_turns * 100:.2f}%')
print(f'From 10 to 19: {from_10_to_19 / total_turns * 100:.2f}%')
print(f'From 20 to 29: {from_20_to_29 / total_turns * 100:.2f}%')
print(f'From 30 to 39: {from_30_to_39 / total_turns * 100:.2f}%')
print(f'From 40 to 50: {from_40_to_50 / total_turns * 100:.2f}%')
print(f'Invalid numbers: {invalid_numbers / total_turns * 100:.2f}%')



