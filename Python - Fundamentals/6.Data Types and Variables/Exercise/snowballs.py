number_of_snowballs = int(input())

highest_value = 0
snowball_weight = 0
snowball_quality = 0
snowball_time_needed = 0

for num in range(number_of_snowballs):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight / time_needed) ** quality

    if snowball_value > highest_value:
        highest_value = snowball_value
        snowball_weight = weight
        snowball_quality = quality
        snowball_time_needed = time_needed

print(f'{snowball_weight} : {snowball_time_needed} = {int(highest_value)} ({snowball_quality})')



