travel_route = input().split("||")
fuel = int(input())
ammunition = int(input())

for act in travel_route:
    act_split = act.split()
    command = act_split[0]

    if command == 'Travel':
        value = int(act_split[1])
        if fuel >= value:
            fuel -= value
            print(f'The spaceship travelled {value} light-years.')
        else:
            print(f'Mission failed.')
            break
    elif command == 'Enemy':
        value = int(act_split[1])
        if ammunition >= value:
            ammunition -= value
            print(f'An enemy with {value} armour is defeated.')
        elif fuel >= (value * 2):
            fuel -= value * 2
            print(f'An enemy with {value} armour is outmaneuvered.')
        else:
            print(f'Mission failed.')
            break
    elif command == 'Repair':
        value = int(act_split[1])
        fuel += value
        ammunition += value * 2
        print(f'Ammunitions added: {value * 2}.')
        print(f'Fuel added: {value}.')
    elif command == 'Titan':
        print(f'You have reached Titan, all passengers are safe.')
        break



