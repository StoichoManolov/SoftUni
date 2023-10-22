pirate_status = [int(x) for x in input().split('>')]
warship_status = [int(x) for x in input().split('>')]
max_health = int(input())
current_health = max_health
pirate_sunken = False
warship_sunken = False

while True:
    command = input()

    if command == 'Retire':
        break
    elif max_health <= 0:
        break

    command_split = command.split()
    act = command_split[0]

    if act == 'Fire':
        index = int(command_split[1])
        damage = int(command_split[2])
        if 0 <= index <= len(warship_status):
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f'You won! The enemy ship has sunken.')
                warship_sunken = True
                break
    elif act == 'Defend':
        index = int(command_split[1])
        end_index = int(command_split[2])
        damage = int(command_split[3])
        if all(x in range(len(pirate_status)) for x in [index, end_index]):
            game_over = False
            for i in range(index, end_index + 1):
                pirate_status[i] -= damage
                if pirate_status[i] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    pirate_sunken = True
                    break

    elif act == 'Repair':
        index = int(command_split[1])
        health = int(command_split[2])
        if 0 <= index < len(pirate_status):
            pirate_status[index] += health
            if max_health < pirate_status[index]:
                pirate_status[index] = max_health
    elif act == 'Status':
        low_health = [x for x in pirate_status if x < max_health // 5]
        count = len(low_health)
        print(f'{count} sections need repair.')

    if pirate_sunken:
        break
    elif warship_sunken:
        break


if command == 'Retire':
    print(f'Pirate ship status: {sum(pirate_status)}')
    print(f'Warship status: {sum(warship_status)}')

