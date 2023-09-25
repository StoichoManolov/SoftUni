number = int(input())
capacity = 255
liters_poured = 0

for num in range(number):
    liters_of_water = int(input())
    liters_poured += liters_of_water

    if capacity < liters_poured:
        liters_poured -= liters_of_water
        print(f'Insufficient capacity!')
else:
    print(liters_poured)
