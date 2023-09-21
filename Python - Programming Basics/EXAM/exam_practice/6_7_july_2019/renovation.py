from math import ceil

height = int(input())
width = int(input())
percent_no_paint = int(input())

is_tired = False
total_walls = height * width * 4
walls_for_painting = ceil(total_walls - ((total_walls * percent_no_paint) / 100))
paintings_left = walls_for_painting

while paintings_left <= walls_for_painting:
    command = input()
    if command == "Tired!":
        is_tired = True
        break
    liters_of_paint = int(command)
    paintings_left -= liters_of_paint
    if paintings_left <= 0:
        break

if is_tired:
    print(f"{paintings_left} quadratic m left.")
elif paintings_left >= 0:
    print("All walls are painted! Great job, Pesho!")
else:
    print(f"All walls are painted and you have {abs(paintings_left)} l paint left!")


