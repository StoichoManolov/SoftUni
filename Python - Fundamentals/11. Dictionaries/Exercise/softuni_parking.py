number = int(input())
parking = {}

for cars in range(number):

    order = input().split()

    command = order[0]
    name = order[1]

    if command == 'register':
        plate = order[2]
        if name not in parking.keys():
            parking[name] = plate
            print(f'{name} registered {plate} successfully')
        else:
            print(f'ERROR: already registered with plate number {parking[name]}')

    elif command == 'unregister':
        if name not in parking.keys():
            print(f'ERROR: user {name} not found')
        else:
            parking.pop(name)
            print(f'{name} unregistered successfully')

for item, value in parking.items():
    print(f'{item} => {value}')