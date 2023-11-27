def drive(car, distance, fuel):
    if cars_info[car_name][1] >= fuel:
        cars_info[car_name][1] -= fuel
        cars_info[car_name][0] += distance
        print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_info[car_name][0] >= 100_000:
            del cars_info[car_name]
            print(f"Time to sell the {car_name}!")
    else:
        print("Not enough fuel to make that ride")


def refuel(car,fuel):
    if cars_info[car][1] + fuel > 75:
        fuel = 75 - cars_info[car][1]
    cars_info[car_name][1] += fuel
    print(f'{car} refueled with {fuel} liters')


def revert(car,kilometers):
    if cars_info[car][0] - kilometers < 10000:
        cars_info[car][0] = 10000
    else:
        cars_info[car][0] -= kilometers
        print(f'{car} mileage decreased by {kilometers} kilometers')


n = int(input())
cars_info = {}

for _ in range(n):
    car_name, *info = (int(x) if x.isdigit() else x for x in input().split("|"))
    cars_info[car_name] = info

while True:
    command = input()

    if command == 'Stop':
        break

    command_split = command.split(' : ')

    act = command_split[0]
    car_name = command_split[1]

    if act == 'Drive':
        distance = int(command_split[2])
        petrol = int(command_split[3])
        drive(car_name,distance,petrol)

    elif act == 'Refuel':
        petrol = int(command_split[2])

        refuel(car_name, petrol)
    elif act == 'Revert':
        distance = int(command_split[2])
        revert(car_name,distance)


for car in cars_info:
    print(f"{car} -> Mileage: {cars_info[car][0]} kms, Fuel in the tank: {cars_info[car][1]} lt.")

