from math import ceil

avg_speed = float(input())
fuel = float(input())

total_distance = 384400 * 2

time_for_distance = ceil(total_distance / avg_speed) + 3
fuel_cost = (fuel * total_distance) / 100

print(f'{time_for_distance}')
print(f'{int(fuel_cost)}')





