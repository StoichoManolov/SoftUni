type_of_fuel = input().lower()
fuel_in_tank = float(input())

if type_of_fuel == 'gas' or type_of_fuel == 'diesel' or type_of_fuel == 'gasoline':
    if fuel_in_tank >= 25:
        print(f'You have enough {type_of_fuel}.')
    elif fuel_in_tank < 25:
        print(f'Fill your tank with {type_of_fuel}!')
else:
    print('Invalid fuel!')